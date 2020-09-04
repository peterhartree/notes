const { description } = require('../../package')
const glob = require('glob');

let markdownFiles = glob.sync('docs/**/*.md').map(f => '/' + f);
// update the docs/**/*.md pattern with your folder structure

console.log('markdown files');
console.log(markdownFiles);

module.exports = {
  /**
   * Ref：https://v1.vuepress.vuejs.org/config/#title
   */
  title: 'Peter\'s notes',
  /**
   * Ref：https://v1.vuepress.vuejs.org/config/#description
   */
  description: description,

  /**
   * Extra tags to be injected to the page HTML `<head>`
   *
   * ref：https://v1.vuepress.vuejs.org/config/#head
   */
  head: [
    ['meta', { name: 'theme-color', content: '#3eaf7c' }],
    ['meta', { name: 'apple-mobile-web-app-capable', content: 'yes' }],
    ['meta', { name: 'apple-mobile-web-app-status-bar-style', content: 'black' }]
  ],

  /**
   * Theme configuration, here is the default theme configuration for VuePress.
   *
   * ref：https://v1.vuepress.vuejs.org/theme/default-theme-config.html
   */
  themeConfig: {
    repo: '',
    editLinks: false,
    docsDir: '',
    editLinkText: '',
    lastUpdated: 'Last updated',
    nav: [
      {
        text: 'People',
        link: '/people/'
      },
      {
        text: 'Journal',
        link: 'https://docs.google.com/document/d/1l3FNWlNUzcpXtend9wrGc3PWSQDj9AwgWcwmOhRsYRY/edit#'
      },
      {
        text: 'Audio',
        link: 'https://thevalmy.com'
      },
      /*
      {
        text: 'Config',
        link: '/config/'
      }
      */
    ],
    sidebar: markdownFiles
    /*
    sidebar: {
      '/guide/': [
        {
          title: 'Guide',
          collapsable: false,
          children: [
            '',
            'using-vue',
          ]
        }
      ],
    }
          */
  },

  /**
   * Apply plugins，ref：https://v1.vuepress.vuejs.org/zh/plugin/
   */
  plugins: {
    '@vuepress/plugin-back-to-top': {},
    '@vuepress/plugin-medium-zoom': {},
    'sitemap': {
      hostname: 'https://pake.web.id'
    }
  }
}
