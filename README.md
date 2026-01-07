digipres.org
============

This repository holds the source files that are used to generate <http://www.digipres.org>.

How it works
------------

The digipres.org site is generated using [GitHub Pages](https://pages.github.com/), which uses the [Jekyll](http://jekyllrb.com/) site generator to create static sites from a set of source files and templates. This repository holds the source material (including various data files in _data as well as HTML or MD files) along with templates used to present the content (in _layouts and _includes).

However, note that some of these source files, particularly the _data files, are not intended to be edited manually. They are generated from various other sources of information via a periodic automated process. The information on formats is drawn from many different sources (e.g. PRONOM and the Archive Team File Formats Wiki).

The code that performs these updates is called [Sentinel](https://github.com/digipres/sentinel).

### digipres.net back-up domain

The same site is also deployed to <https://digipres.net/> using [Netlify](https://www.netlify.com/) (account owned by [@anjackson](https://github.com/anjackson/)). This allows [DecapCMS](https://decapcms.org/) to be used to support editing the site (see below). n.b. this is because Netlify helps with the [authentication process](https://decapcms.org/docs/github-backend/).

Using Netlify also has the advantage that any changes proposed to the site on GitHub are [automatically deployed on a test service so they can be reviewed](https://docs.netlify.com/deploy/deploy-types/deploy-previews/).

Contributing to this site
-------------------------

There are a couple of ways to directly contribute to the site content:

- Some content, like local groups, can be edited via a [basic CMS](https://digipres.net/admin/). A GitHub account is required to log in, and the editing tool will open a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) on your behalf.
- You can propose changes to all the pages on this site by [editing them using the GitHub user interface](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files).

### Local Development

For more complicated changes, you can build the site locally.

* Fork it.
* Install Ruby > 3 and the bundle gem.
* Install Jekyll and required dependencies: `bundle install`
* Run Jekyll and supporting services in development mode: `./dev.sh`
* Commit changes to your fork.
* Submit a pull request, describing the change.

