<template>
  <v-data-iterator
    :items="items"
    :items-per-page="itemsPerPage"
    :loading="loading"
    :class="elevated ? 'elevation-2' : ''"
    :search="search"
    :sort-by.sync="sortBy"
    :sort-desc.sync="sortDesc"
    multi-sort
    @update:sort-by="handleSortChange"
    @update:sort-desc="handleSortChange"
    :show-select="showSelect"
    selectable-key="selectable"
    @toggle-select-all="handleToggleAll"
  >
    <!-- Bar template -->
    <template #header>
      <c-r-u-d-bar
        v-bind="$attrs"
        v-on="$listeners"
        @mode="$emit('mode', $event)"
        @loading="handleLoading"
        @items="handleItems"
        @last-query="$emit('lastQuery', $event)"
        @search="search = $event"
        @selectable="showSelect = true"
        :selection="selection"
        @selection="handleSelection"
        @deletable="$emit('deletable', $event)"
      >
        <template #filters="{ attrs, on }">
          <slot name="filters" :attrs="attrs" :on="on" />
        </template>

        <template
          v-for="header in computedHeaders"
          #[fieldSlot(header)]="{ item, isCreate, on, attrs }"
        >
          <slot
            :name="fieldSlot(header)"
            :attrs="attrs"
            :on="on"
            :item="item"
            :is-create="isCreate"
          />
        </template>
        <template #additionalActions="{ attrs, on }">
          <slot name="additionalActions" :attrs="attrs" :on="on" />
        </template>
      </c-r-u-d-bar>
    </template>

    <template #default="slotProps">
      <slot name="default" v-bind="slotProps" />
    </template>
  </v-data-iterator>
</template>

<script>
import CRUDBar from "./CRUDBar.vue";

import syncSortMixin from "../../mixins/syncSortMixin.js";

// TODO: props, data & methods are a subset of CRUDList's -> share?

export default {
  name: "CRUDIterator",
  components: {
    CRUDBar,
  },
  mixins: [syncSortMixin],
  props: {
    /**
     * Elevate the iterator?
     * @values true, false
     */
    elevated: {
      type: Boolean,
      required: false,
      default: true,
    },
    /**
     * Number of items shown per page
     * @values natural number
     */
    itemsPerPage: {
      type: Number,
      required: false,
      default: 15,
    },
  },
  emits: ["mode", "lastQuery", "deletable", "loading", "items", "selection"],
  data() {
    return {
      items: [],
      // Loading state
      loading: false,
      // Search
      search: "",
      // Item selection
      showSelect: false,
      selection: [],
      allSelected: false,
    };
  },
  computed: {
    computedHeaders() {
      return "headers" in this.$attrs
        ? this.$attrs.headers.filter((header) => !header.disableEdit)
        : [];
    },
  },
  methods: {
    handleLoading(state) {
      this.loading = state;
      // Pass on; documented in query/mutateMixin.
      this.$emit("loading", state);
    },
    handleItems(items) {
      this.items = items;
      // Pass on; documented in queryMixin.
      this.$emit("items", items);
    },
    handleSelection(selection) {
      this.selection = selection;
      // Pass on; documented in CRUDBar.
      this.$emit("selection", selection);
    },
    // Item selection
    handleToggleAll({ items, value }) {
      if (value) {
        // There is a bug in vuetify: items contains all elements, even those that aren't selectable
        this.handleSelection(items.filter((item) => item.selectable));
      } else {
        this.handleSelection([]);
      }
      this.allSelected = value;
    },
    // Template names
    fieldSlot(header) {
      return header.value + ".field";
    },
  },
};
</script>
