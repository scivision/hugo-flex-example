# Hugo-flex theme example

This is an example site for [hugo-flex theme](https://github.com/de-souza/hugo-flex).
Hugo-Flex is a JavaScript-free theme with PageSpeed 100.
This is important for having a really fast website without using AMP.
I have built a top 100,000 website (https://www.scivision.dev) using hugo-flex.

The advantages of static site generators like Hugo include that you write pages in very simple Markdown .md syntax in the [content/blog](./content/blog) directory, and images and other files you desire to serve under [static/](./static) directory.
Static pages (like [about.md](./content/about.md)) go in [content/](./content) directory itself.

Images, Twitter tweets, YouTube videos, etc. are inlined via Hugo
[shortcodes](https://gohugo.io/content-management/shortcodes/#use-hugo-s-built-in-shortcodes).

## Configuring

1. [Install Hugo](https://gohugo.io/overview/installing/)
2. Make a copy of this template repo by clicking the [Use this Template](https://help.github.com/en/articles/creating-a-repository-from-a-template) button.
3. Add the Hugo-Flex theme
    ```bash
    git submodule add https://github.com/de-souza/hugo-flex.git themes/hugo-flex
    ```
4. Run Hugo and point your web browser to http://localhost:1313
    ```bash
    hugo server
    ```
5. Edit the website configuration in config.toml (or config.yaml). You may have to restart `hugo server` if you make major changes.

## Deploying

Note:

* in the following discussion replace "username" with your GitHub username.
* in config.toml, be sure "baseUrl" is set for your username/reponame or it will not deploy correctly.


You can build and deploy to
[Github Pages](https://gohugo.io/hosting-and-deployment/hosting-on-github/).
For advanced / higher traffic pages (1 million + views/year) you might consider
[Netlify](https://www.scivision.dev/github-pages-to-netlify/).
Most individual users can simply use GitHub Pages.

A simple way is to use the [deploy.py](./deploy.py) script.
It builds the pages on your laptop, adds them to Git history and pushes to GitHub Pages.
For moderate to large websites, consider continuous deployment methods like
[Netlify](https://gohugo.io/hosting-and-deployment/hosting-on-netlify/).

1. Configure GitHub Pages Settings for your repo to have Source: "master branch /docs folder"
2. run "python deploy.py"
3. browse to https://username.github.io/hugo-flex-example to see your demo site.

When satisfied with the demo site, rename the repository to username.github.io and then your visitors can simply browse https://username.github.io

### Domain name

To have your web address be https://janedoe.example or similar, you must purchase a domain name (from
[Google Domains](https://domains.google)
for example) and then
[configure DNS](https://help.github.com/en/articles/setting-up-a-www-subdomain)
to point to https://username.github.io

### Private history

To keep the configuration and history of your website private, you can set the webpage GitHub repo to be "Private", while deploying a public webpage.
This is recommended as in some cases, Google and other search engines will show the website Git repo in the search results alongside the actual desired website.
