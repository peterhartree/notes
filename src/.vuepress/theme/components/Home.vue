<template>
  <main
    class="home"
    :aria-labelledby="data.heroText !== null ? 'main-title' : null"
  >
    <header class="hero">
      <img
        v-if="data.heroImage"
        :src="$withBase(data.heroImage)"
        :alt="data.heroAlt || 'hero'"
      >

      <h1
        v-if="data.heroText !== null"
        id="main-title"
      >
        {{ data.heroText || $title || 'Hello' }}
      </h1>
      <div
      v-if="data.footer"
      class="footer"
      v-html="data.footer"
      ></div>

      <p
        v-if="data.actionText && data.actionLink"
        class="action"
      >
        <NavLink
          class="action-button"
          :item="actionLink"
        />
      </p>
    </header>

    <div
      v-if="data.features && data.features.length"
      class="features"
    >
      <div
        v-for="(feature, index) in data.features"
        :key="index"
        class="feature"
      >
        <h2>{{ feature.title }}</h2>
        <p v-html="feature.details"></p>
        <p
          v-if="feature.button"
          class="action"
        >
          <NavLink
            class="action-button"
            :item="feature.button"
          />
        </p>
      </div>
    </div>

    <Content class="theme-default-content custom" />

    <div class="whats-new">
      <h2>Recently added</h2>

      <div class="notes">
        <p>My notes:</p>
        <ul id="list_notes">
          <li><router-link to="/misc/where-am-i.html">Where am I?</router-link></li>
          <li><router-link to="/people/tyler-cowen.html">Tyler Cowen</router-link ></li>
          <li><router-link to="/people/stewart-brand.html">Stewart Brand</router-link ></li>
          <li><router-link to="/people/susan-wolf.html">Susan Wolf</router-link ></li>
          <li><router-link to="/people/bernard-williams.html">Bernard Williams</router-link ></li>
          <li><router-link to="/misc/value-reasons-self.html">Value, reasons, self</router-link ></li>
        </ul>
      </div>

      <div class="podcasts" style="display: none;">
        <p>Interesting podcasts:</p>
        <ul id="list_podcasts">
          <li>Loading...</li>
        </ul>
      </div>
    </div>
    <script>
    </script>
  </main>
</template>

<script>
import NavLink from '@theme/components/NavLink.vue'

export default {
  name: 'Home',

  components: { NavLink },

  computed: {
    data () {
      return this.$page.frontmatter
    },

    actionLink () {
      return {
        link: this.data.actionLink,
        text: this.data.actionText
      }
    }
  },
  created() {
    /*
    fetch('https://listen.thevalmy.com/')
      .then(response => response.text())
      .then(str => new window.DOMParser().parseFromString(str, 'text/xml'))
      .then(data => {
        const items = data.querySelectorAll('item');
        let html = ``;
        let episodeNumber = ``;
        const episodeCount = items.length;
        items.forEach(function(el, index) {
          episodeNumber = episodeCount - index;
          if(index < 6) {
          html += `
            <li>
                <a href="https://thevalmy.com/${episodeNumber}" target="_blank" rel="noopener">
                  ${el.querySelector("title").innerHTML}
                </a>
            </li>
          `;
          }
        });
        document.getElementById('list_podcasts').innerHTML = html;
      });
    */
  }
}
</script>

<style lang="stylus">
.home
  padding $navbarHeight 2rem 0
  max-width $homePageWidth
  margin 0px auto
  display block
  .hero
    img
      max-width: 100%
      max-height 280px
      display block
      margin 3rem auto 1.5rem
    h1
      font-size 3rem
    h1, .description, .action
      margin 3rem auto 1.5rem auto
    .description
      max-width 35rem
      font-size 1.6rem
      line-height 1.3
      color lighten($textColor, 40%)
    .action-button
      display inline-block
      font-size 1.2rem
      color #fff
      background-color $accentColor
      padding 0.8rem 1.6rem
      border-radius 4px
      transition background-color .1s ease
      box-sizing border-box
      border-bottom 1px solid darken($accentColor, 10%)
      &:hover
        background-color lighten($accentColor, 10%)
  .features
    padding 1.2rem 0
    margin-top 2.5rem
    display flex
    display none
    flex-wrap wrap
    align-items flex-start
    align-content stretch
    justify-content space-between
  .whats-new
    margin-bottom 8rem
    h2
      font-size 2rem
      margin-top 3rem
      margin-bottom 0rem
  .notes
    width 30%
    float left
  .podcasts
    width 70%
    float left
  .feature
    flex-grow 1
    flex-basis 30%
    max-width 30%
    h2
      font-size 1.4rem
      border-bottom none
      padding-bottom 0


@media (max-width: $MQMobile)
  .home
    .podcasts, .notes
      width 100%
    .features
      flex-direction column
    .feature
      max-width 100%
      padding 0 2.5rem

@media (max-width: $MQMobileNarrow)
  .home
    padding-left 1rem
    padding-right 1rem
    .hero
      img
        max-height 210px
        margin 2rem auto 1.2rem
      h1
        font-size 2rem
      h1, .description, .action
        margin 1.2rem auto
      .description
        font-size 1.2rem
      .action-button
        font-size 1rem
        padding 0.6rem 1.2rem
    .feature, .whats-new
      h2
        font-size 1.25rem
</style>
