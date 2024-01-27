<template>
  <v-menu
    ref="menu"
    v-model="menu"
    :close-on-content-click="false"
    transition="scale-transition"
    offset-y
    min-width="auto"
    eager
  >
    <template #activator="{ on, attrs }">
      <v-text-field
        v-model="color"
        v-bind="$attrs"
        v-on="$listeners"
        placeholder="#AABBCC"
        :rules="rules"
      >
        <template #prepend-inner>
          <v-icon :color="color" v-bind="attrs" v-on="on"> mdi-circle </v-icon>
        </template>
      </v-text-field>
    </template>
    <v-color-picker v-if="menu" v-model="color" ref="picker"></v-color-picker>
  </v-menu>
</template>

<script>
export default {
  name: "DateField",
  extends: "v-text-field",
  data() {
    return {
      menu: false,
      rules: [
        (value) =>
          /^(#([0-9a-f]{3,4}|[0-9a-f]{6}|[0-9a-f]{8}))?$/i.test(value) ||
          this.$t("forms.errors.invalid_color"),
      ],
    };
  },
  props: {
    value: {
      type: String,
      default: undefined,
    },
  },
  computed: {
    color: {
      get() {
        return this.value;
      },
      set(newValue) {
        this.$emit("input", newValue);
      },
    },
  },
};
</script>

<style scoped></style>
