# -*- coding: utf-8 -*-

from aws_console_url_search.dataset import (
    ServiceDocument,
    service_downloader,
    service_dataset,
    RegionDocument,
    region_downloader,
    region_dataset,
    preprocess_query,
)


class TestServiceDataset:
    def test_downloader(self):
        docs = service_downloader()

    def test_searcher(self):
        docs = service_dataset.search(query="ec2 inst")
        assert docs[0]["id"] == "ec2-instances"

        docs = service_dataset.search(query="s3 bucket")
        assert docs[0]["id"] == "s3-buckets"


class TestRegionDataset:
    def test_downloader(self):
        docs = region_downloader()

    def test_searcher(self):
        docs = region_dataset.search(query="us east")
        assert docs[0]["id"] == "us-east-1"


if __name__ == "__main__":
    from aws_console_url_search.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url_search.dataset", preview=False)
