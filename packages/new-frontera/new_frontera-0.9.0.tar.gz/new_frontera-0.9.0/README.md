# new_frontera

[![pypi](https://img.shields.io/pypi/v/new_frontera)](https://pypi.org/project/new_frontera/)
[![python versions](https://img.shields.io/pypi/pyversions/new_frontera.svg)](https://pypi.org/project/new_frontera/)
[![Build Status](https://app.travis-ci.com/ZeroCool940711/new-new_frontera.svg?branch=master)](https://app.travis-ci.com/ZeroCool940711/new-new_frontera)
[![codecov](https://codecov.io/gh/scrapinghub/new_frontera/branch/master/graph/badge.svg)](https://codecov.io/gh/scrapinghub/new_frontera)

## Overview

new_frontera is a web crawling framework consisting of [crawl frontier](http://nlp.stanford.edu/IR-book/html/htmledition/the-url-frontier-1.html), and distribution/scaling primitives, allowing to build a large scale online web crawler. 

new_frontera takes care of the logic and policies to follow during the crawl. It stores and prioritizes links extracted by 
the crawler to decide which pages to visit next, and capable of doing it in distributed manner.

## Main features

- Online operation: small requests batches, with parsing done right after fetch.
- Pluggable backend architecture: low-level backend access logic is separated from crawling strategy.
- Two run modes: single process and distributed.
- Built-in SqlAlchemy, Redis and HBase backends.
- Built-in Apache Kafka and ZeroMQ message buses.
- Built-in crawling strategies: breadth-first, depth-first, Discovery (with support of robots.txt and sitemaps).
- Battle tested: our biggest deployment is 60 spiders/strategy workers delivering 50-60M of documents daily for 45 days, without downtime,
- Transparent data flow, allowing to integrate custom components easily using Kafka.
- Message bus abstraction, providing a way to implement your own transport (ZeroMQ and Kafka are available out of the box).
- Optional use of Scrapy for fetching and parsing.
- 3-clause BSD license, allowing to use in any commercial product.
- Python 3 support.

## Installation

Development version:

```bash
$ pip install git+https://github.com/ZeroCool940711/new_frontera.git
```

or from PyPi:

```bash
$ pip install new-frontera
```

## Documentation

- [Main documentation at RTD](http://frontera.readthedocs.org/)
- [EuroPython 2015 slides](http://www.slideshare.net/sixtyone/fronteraopen-source-large-scale-web-crawling-framework)
- [BigDataSpain 2015 slides](https://speakerdeck.com/scrapinghub/frontera-open-source-large-scale-web-crawling-framework)

## Community

Join our Google group at https://groups.google.com/a/scrapinghub.com/forum/#!forum/frontera or check GitHub issues and 
pull requests.
