<template>
  <mobile-fullscreen-dialog v-model="dialog">
    <template #title>
      <!-- @slot Delete dialog title slot -->
      <slot name="title">
        {{ $t(confirmI18nKey) }}
      </slot>
    </template>
    <template #content>
      <!-- @slot Delete dialog body slot -->
      <slot name="body">
        <ul class="text-body-1">
          <li v-for="(item, idx) in items" :key="idx">
            {{ nameOfItem(item) }}
          </li>
        </ul>
      </slot>
    </template>
    <template #actions>
      <cancel-button @click="handleCancel" :disabled="loading">
        <!-- @slot Delete dialog cancel button slot -->
        <slot name="cancelContent">
          <v-icon left>$cancel</v-icon>
          {{ $t("actions.cancel") }}
        </slot>
      </cancel-button>
      <delete-button @click="handleDelete" :disabled="loading">
        <!-- @slot Delete dialog delete button slot -->
        <slot name="deleteContent" />
      </delete-button>
    </template>
  </mobile-fullscreen-dialog>
</template>

<script>
import CancelButton from "../buttons/CancelButton.vue";
import DeleteButton from "../buttons/DeleteButton.vue";
import MobileFullscreenDialog from "./MobileFullscreenDialog.vue";

import deleteMixin from "../../../mixins/deleteMixin.js";

/**
 * This component provides a form for deleting objects via graphQL (via deleteMixin)
 */
export default {
  name: "DeleteDialog",
  components: {
    CancelButton,
    DeleteButton,
    MobileFullscreenDialog,
  },
  mixins: [deleteMixin],
  props: {
    /**
     * Dialog state (open or closed)
     * @model
     * @values true,false
     */
    value: {
      type: Boolean,
      required: true,
    },
    /**
     * Items awaiting confirmation for deletion
     */
    items: {
      type: Array,
      required: false,
      default: () => [],
    },
    /**
     * The item's name property displayed in confirm delete dialog.
     */
    itemAttribute: {
      type: String,
      required: false,
      default: "name",
    },
    /**
     * Message shown after successful delete.
     */
    deleteSuccessMessageI18nKey: {
      type: String,
      required: false,
      default: "status.object_delete_success",
    },
  },
  emits: ["cancel"],
  computed: {
    dialog: {
      get() {
        return this.value;
      },
      set(val) {
        this.$emit("input", val);
      },
    },
    confirmI18nKey() {
      return this.items.length > 1
        ? "actions.confirm_deletion_multiple"
        : "actions.confirm_deletion";
    },
  },
  data() {
    return {
      // Loading state
      loading: false,
    };
  },
  methods: {
    nameOfItem(item) {
      return this.itemAttribute in item || {}
        ? item[this.itemAttribute]
        : item.toString();
    },
    handleDelete() {
      this.delete(this.items);
      this.dialog = false;
    },
    handleCancel() {
      this.dialog = false;
      /**
       * Emitted when user cancels
       */
      this.$emit("cancel");
    },
  },
  mounted() {
    this.$on("loading", (status) => {
      this.loading = status;
    });
    this.$on("save", () => {
      this.dialog = false;
      this.$toastSuccess(this.deleteSuccessMessageI18nKey);
    });
  },
};
</script>
