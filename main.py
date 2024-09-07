import logging

from nerfw import NerFW

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    ner = NerFW()
    ner.ui.set_background(
        "tests/integration_testing/test_data/anime-night-sky-illustration.jpg"
    )
    ner.run()
