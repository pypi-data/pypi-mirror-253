/**
 * This mixin provides generic item query via graphQL.
 * The query result is available in items.
 */
export default {
  props: {
    /**
     * The graphQL query
     */
    gqlQuery: {
      type: Object,
      required: true,
    },
    /**
     * Optional arguments to graphQL query
     */
    // UPDATE NOTICE: Name change from additionalQueryArgs (prop was so far not used anyway)
    gqlAdditionalQueryArgs: {
      type: Object,
      required: false,
      default: () => ({}),
    },
    /**
     * OrderBy directive used in the graphQL query
     */
    gqlOrderBy: {
      type: Array,
      required: false,
      default: () => [],
    },
    /**
     * Filter object used in the graphQL query
     */
    gqlFilters: {
      type: Object,
      required: false,
      default: () => ({}),
    },
    /**
     * Transform function for the data returned by the query
     */
    getGqlData: {
      type: Function,
      required: false,
      default: (item) => item,
    },
  },
  emits: ["loading", "items", "lastQuery"],
  data() {
    return {
      additionalFilters: {},
      lastQuery: {},
    };
  },
  methods: {
    handleItems(items) {
      return items;
    },
  },
  apollo: {
    items() {
      return {
        query: this.gqlQuery,
        variables() {
          const orderBy = this.gqlOrderBy.length
            ? { orderBy: this.gqlOrderBy }
            : {};
          const filters =
            Object.keys(this.gqlFilters).length ||
            Object.keys(this.additionalFilters).length
              ? {
                  filters: JSON.stringify({
                    ...this.gqlFilters,
                    ...this.additionalFilters,
                  }),
                }
              : {};
          return {
            ...this.gqlAdditionalQueryArgs,
            ...orderBy,
            ...filters,
          };
        },
        watchLoading(loading) {
          /**
           * Emitted when graphQL query starts or finishes loading
           *
           * @property {boolean} status shows whether loading or not
           */
          this.$emit("loading", loading);
        },
        error: (error) => {
          this.handleError(error);
        },
        update: (data) => {
          this.lastQuery = this.$apollo.queries.items;
          /**
           * Emits the last query
           * Use this to update the cache
           *
           * @property {Object} graphQL query
           */
          this.$emit("lastQuery", this.lastQuery);
          const items = this.handleItems(this.getGqlData(data.items));
          /**
           * Emits updated items
           * either from a graphQL query
           * or if the cached result was updated.
           *
           * @property {array} Query restult
           */
          this.$emit("items", items);
          return items;
        },
      };
    },
  },
};
