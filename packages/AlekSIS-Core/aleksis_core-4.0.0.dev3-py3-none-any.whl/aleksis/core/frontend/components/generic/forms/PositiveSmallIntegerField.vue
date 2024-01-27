<template>
  <v-text-field
    v-bind="$attrs"
    v-on="on"
    :rules="rules"
    type="number"
    inputmode="decimal"
  ></v-text-field>
</template>

<script>
export default {
  name: "PositiveSmallIntegerField",
  extends: "v-text-field",
  methods: {
    handleInput(event) {
      let num = parseInt(event);
      if (!isNaN(num) && num >= 0 && num <= 32767 && num % 1 === 0) {
        this.$emit("input", parseInt(event));
      }
    },
  },
  data() {
    return {
      rules: [
        (value) =>
          !value ||
          !isNaN(parseInt(value)) ||
          this.$t("forms.errors.not_a_number"),
        (value) =>
          !value ||
          value % 1 === 0 ||
          this.$t("forms.errors.not_a_whole_number"),
        (value) =>
          !value ||
          parseInt(value) >= 0 ||
          this.$t("forms.errors.number_too_small"),
        (value) =>
          !value ||
          parseInt(value) <= 32767 ||
          this.$t("forms.errors.number_too_big"),
      ],
    };
  },
  computed: {
    on() {
      return {
        ...this.$listeners,
        input: this.handleInput,
      };
    },
  },
};
</script>

<style scoped></style>
