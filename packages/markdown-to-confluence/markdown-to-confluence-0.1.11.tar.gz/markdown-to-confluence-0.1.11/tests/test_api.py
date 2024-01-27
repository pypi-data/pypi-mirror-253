import logging
import os
import os.path
import shutil
import unittest

from md2conf.api import ConfluenceAPI, ConfluenceAttachment, ConfluencePage
from md2conf.application import Application
from md2conf.converter import (
    ConfluenceDocument,
    ConfluenceDocumentOptions,
    sanitize_confluence,
)
from md2conf.properties import ConfluenceProperties

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(funcName)s [%(lineno)d] - %(message)s",
)


class TestAPI(unittest.TestCase):
    out_dir: str

    def setUp(self) -> None:
        self.out_dir = os.path.join(os.getcwd(), "tests", "output")
        os.makedirs(self.out_dir, exist_ok=True)

    def tearDown(self) -> None:
        shutil.rmtree(self.out_dir)

    def test_markdown(self) -> None:
        document = ConfluenceDocument(
            os.path.join(os.getcwd(), "sample", "example.md"),
            ConfluenceDocumentOptions(ignore_invalid_url=True),
            {},
        )
        self.assertListEqual(document.links, [])
        self.assertListEqual(
            document.images,
            ["figure/interoperability.png", "figure/interoperability.png"],
        )

        with open(os.path.join(self.out_dir, "document.html"), "w") as f:
            f.write(document.xhtml())

    def test_find_page_by_title(self) -> None:
        with ConfluenceAPI() as api:
            id = api.get_page_id_by_title("Publish to Confluence")
            self.assertEqual(id, "85668266616")

    def test_switch_space(self) -> None:
        with ConfluenceAPI(ConfluenceProperties(space_key="PLAT")) as api:
            with api.switch_space("DAP"):
                id = api.get_page_id_by_title("Publish to Confluence")
                self.assertEqual(id, "85668266616")

    def test_get_page(self) -> None:
        with ConfluenceAPI() as api:
            page = api.get_page("85668266616")
            self.assertIsInstance(page, ConfluencePage)

        with open(os.path.join(self.out_dir, "page.html"), "w") as f:
            f.write(sanitize_confluence(page.content))

    def test_get_attachment(self) -> None:
        with ConfluenceAPI() as api:
            data = api.get_attachment_by_name(
                "85668266616", "figure/interoperability.png"
            )
            self.assertIsInstance(data, ConfluenceAttachment)

    def test_upload_attachment(self) -> None:
        with ConfluenceAPI() as api:
            api.upload_attachment(
                "85668266616",
                os.path.join(os.getcwd(), "sample", "figure", "interoperability.png"),
                "figure/interoperability.png",
                "A sample figure",
            )

    def test_synchronize(self) -> None:
        with ConfluenceAPI() as api:
            Application(
                api, ConfluenceDocumentOptions(ignore_invalid_url=True)
            ).synchronize(os.path.join(os.getcwd(), "sample", "example.md"))

    def test_synchronize_page(self) -> None:
        with ConfluenceAPI() as api:
            Application(
                api, ConfluenceDocumentOptions(ignore_invalid_url=True)
            ).synchronize_page(os.path.join(os.getcwd(), "sample", "example.md"))

    def test_synchronize_directory(self) -> None:
        with ConfluenceAPI() as api:
            Application(
                api, ConfluenceDocumentOptions(ignore_invalid_url=True)
            ).synchronize_directory(os.path.join(os.getcwd(), "sample"))

    def test_synchronize_create(self) -> None:
        dir = os.path.join(self.out_dir, "markdown")
        os.makedirs(dir, exist_ok=True)

        child = os.path.join(dir, "child.md")
        with open(child, "w") as f:
            f.write(
                "This is a document without an explicitly linked Confluence document.\n"
            )

        with ConfluenceAPI() as api:
            Application(
                api,
                ConfluenceDocumentOptions(
                    ignore_invalid_url=True, root_page_id="86090481730"
                ),
            ).synchronize_directory(dir)

        with open(child, "r") as f:
            self.assertEqual(
                f.read(),
                "<!-- confluence-page-id: 86269493445 -->\n"
                "<!-- confluence-space-key: DAP -->\n"
                "This is a document without an explicitly linked Confluence document.\n",
            )


if __name__ == "__main__":
    unittest.main()
