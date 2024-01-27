<script setup>
import CreateButton from "../../generic/buttons/CreateButton.vue";
import DateTimeField from "../../generic/forms/DateTimeField.vue";
import DialogObjectForm from "../../generic/dialogs/DialogObjectForm.vue";
import EditButton from "../../generic/buttons/EditButton.vue";
import RecurrenceField from "../../generic/forms/RecurrenceField.vue";
</script>

<template>
  <dialog-object-form
    v-model="dialogOpen"
    :get-create-data="getData"
    :get-patch-data="getData"
    :default-item="defaultItem"
    :edit-item="editItem"
    :gql-create-mutation="gqlCreateMutation"
    :gql-patch-mutation="gqlPatchMutation"
    :is-create="!editItem"
    :fields="fields"
    :create-item-i18n-key="createItemI18nKey"
    :edit-item-i18n-key="editItemI18nKey"
    @save="$emit('save')"
  >
    <template #activator="{ props }">
      <create-button
        v-if="!editItem"
        color="secondary"
        @click="requestDialog"
        :disabled="dialogOpen"
        fab
        large
        bottom
        fixed
        right
      >
        <v-icon>$plus</v-icon>
      </create-button>
      <edit-button
        v-else
        color="secondary"
        outlined
        @click="requestDialog"
        :disabled="dialogOpen"
      />
    </template>

    <!-- eslint-disable-next-line vue/valid-v-slot -->
    <template #title.field="{ attrs, on }">
      <div aria-required="true">
        <v-text-field v-bind="attrs" v-on="on" required />
      </div>
    </template>

    <!-- eslint-disable-next-line vue/valid-v-slot -->
    <template #description.field="{ attrs, on }">
      <v-textarea v-bind="attrs" v-on="on" />
    </template>

    <!-- eslint-disable-next-line vue/valid-v-slot -->
    <template #datetimeStart.field="{ attrs, on }">
      <div aria-required="true">
        <date-time-field v-bind="attrs" v-on="on" required />
      </div>
    </template>

    <!-- eslint-disable-next-line vue/valid-v-slot -->
    <template #datetimeEnd.field="{ attrs, on }">
      <div aria-required="true">
        <date-time-field v-bind="attrs" v-on="on" required />
      </div>
    </template>

    <!-- eslint-disable-next-line vue/valid-v-slot -->
    <template #recurrences.field="{ attrs, on }">
      <recurrence-field v-bind="attrs" v-on="on" :start-date="DateTime.now()" />
    </template>

    <!-- eslint-disable-next-line vue/valid-v-slot -->
    <template #persons.field="{ attrs, on }">
      <v-autocomplete
        multiple
        :items="persons"
        item-text="fullName"
        item-value="id"
        v-bind="attrs"
        v-on="on"
        :loading="$apollo.queries.persons.loading"
      />
    </template>

    <!-- eslint-disable-next-line vue/valid-v-slot -->
    <template #groups.field="{ attrs, on }">
      <v-autocomplete
        multiple
        :items="groups"
        item-text="shortName"
        item-value="id"
        v-bind="attrs"
        v-on="on"
        :loading="$apollo.queries.groups.loading"
      />
    </template>
  </dialog-object-form>
</template>

<script>
import {
  createPersonalEvents,
  deletePersonalEvents,
  updatePersonalEvents,
  gqlPersons,
  gqlGroups,
} from "./personalEvent.graphql";

import permissionsMixin from "../../../mixins/permissions.js";

import { DateTime } from "luxon";

export default {
  name: "PersonalEventDialog",
  data() {
    return {
      createItemI18nKey: "personal_events.create_title",
      editItemI18nKey: "personal_events.edit_title",
      gqlCreateMutation: createPersonalEvents,
      gqlPatchMutation: updatePersonalEvents,
      gqlDeleteMutation: deletePersonalEvents,
      defaultItem: {
        title: "",
        description: "",
        datetimeStart: DateTime.now()
          .startOf("minute")
          .toISO({ suppressSeconds: true }),
        datetimeEnd: DateTime.now()
          .startOf("minute")
          .plus({ hours: 1 })
          .toISO({ suppressSeconds: true }),
        recurrences: "",
        persons: [],
        groups: [],
      },
      dialogOpen: false,
    };
  },
  props: {
    editItem: {
      type: Object,
      required: false,
      default: undefined,
    },
  },
  apollo: {
    persons: {
      query: gqlPersons,
      skip() {
        return !this.checkPermission(
          "core.create_personal_event_with_invitations_rule",
        );
      },
    },
    groups: {
      query: gqlGroups,
      skip() {
        return !this.checkPermission(
          "core.create_personal_event_with_invitations_rule",
        );
      },
    },
  },
  mixins: [permissionsMixin],
  methods: {
    getData(item) {
      return {
        id: item.id,
        title: item.title,
        description: item.description,
        location: item.location,
        datetimeStart: item.datetimeStart,
        datetimeEnd: item.datetimeEnd,
        recurrences: item.recurrences,
        persons: this.checkPermission(
          "core.create_personal_event_with_invitations_rule",
        )
          ? item.persons
          : [],
        groups: this.checkPermission(
          "core.create_personal_event_with_invitations_rule",
        )
          ? item.groups
          : [],
      };
    },
    requestDialog() {
      this.dialogOpen = true;
    },
  },
  computed: {
    fields() {
      const fields = [
        {
          text: this.$t("personal_events.title"),
          value: "title",
          cols: 12,
        },
        {
          text: this.$t("personal_events.datetime_start"),
          value: "datetimeStart",
        },
        {
          text: this.$t("personal_events.datetime_end"),
          value: "datetimeEnd",
        },
        {
          text: this.$t("personal_events.recurrences"),
          value: "recurrences",
          cols: 12,
        },
        {
          text: this.$t("personal_events.description"),
          value: "description",
          cols: 12,
        },
        {
          text: this.$t("personal_events.location"),
          value: "location",
          cols: 12,
        },
      ];
      if (
        this.checkPermission("core.create_personal_event_with_invitations_rule")
      ) {
        fields.push(
          {
            text: this.$t("personal_events.persons"),
            value: "persons",
          },
          {
            text: this.$t("personal_events.groups"),
            value: "groups",
          },
        );
      }
      return fields;
    },
  },
  mounted() {
    this.addPermissions(["core.create_personal_event_with_invitations_rule"]);
  },
};
</script>
