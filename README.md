# Hugo-flex theme example

This is an example from scratch using [hugo-flex theme](https://github.com/de-souza/hugo-flex).
Hugo-Flex is a JavaScript-free theme with Google PageSpeed 100.
This is important for having a really fast website without using AMP.
We have built a top 500,000 website (https://www.scivision.dev) using hugo-flex.

Static site generators like Hugo build an arbitrarily simple or complex website from:

* simple Markdown .md syntax in the [content/posts](./content/posts) directory
* images and other files under [static/](./static) directory
* static pages like about.md go in [content/](./content) directory

Images, Twitter tweets, YouTube videos, etc. are inlined via Hugo
[shortcodes](https://gohugo.io/content-management/shortcodes/#use-hugo-s-built-in-shortcodes).

## Configuring

1. [Install Hugo](https://gohugo.io/overview/installing/)
2. Make a copy of this template repo by clicking the [Use this Template](https://help.github.com/en/articles/creating-a-repository-from-a-template) button.
3. `git clone --recurse-submodules` your copy to your laptop and change to that directory.
4. Run Hugo and point your web browser to http://localhost:1313
    ```bash
    hugo serve
    ```
5. Edit the website configuration in config.toml (or config.yaml). You may have to restart `hugo serve` if you make major changes.

## Deploying

Note:

* in the following discussion replace "username" with your GitHub username.
* in config.toml, be sure "baseUrl" is set for your username/reponame or it will not deploy correctly.


You can build and deploy to
[Github Pages](https://gohugo.io/hosting-and-deployment/hosting-on-github/).
For advanced / higher traffic pages (1 million + views/year) you might consider
[Netlify](https://www.scivision.dev/github-pages-to-netlify/).
Most individual users can simply use GitHub Pages.

### deploy Hugo to GitHub Pages

For GitHub Pages with Hugo, build the HTML on your laptop.

One-time: configure GitHub Pages Settings for your repo to have Source: "master branch /docs folder".

Each time website is updated, from the top-level website repo directory:

1. Build site, with HTML output to docs/ per config.yaml:

  ```sh
  hugo --source .
  ```
2. Add changes to git.

  ```sh
  git add docs
  ```
3. Commit changes.

  ```sh
  git commit -m "updated website"
  ```
4. Push site to GitHub Pages

  ```sh
  git push
  ```


Browse to https://username.github.io/hugo-flex-example to see your demo site.

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
