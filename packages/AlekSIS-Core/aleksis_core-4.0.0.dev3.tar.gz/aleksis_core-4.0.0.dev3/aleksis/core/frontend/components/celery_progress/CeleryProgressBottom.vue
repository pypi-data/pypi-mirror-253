<template>
  <v-bottom-sheet
    :value="show"
    persistent
    hide-overlay
    max-width="400px"
    ref="sheet"
  >
    <v-expansion-panels accordion v-model="open">
      <v-expansion-panel>
        <v-expansion-panel-header color="primary" class="white--text px-4">
          {{
            $tc("celery_progress.running_tasks", numberOfTasks, {
              number: numberOfTasks,
            })
          }}
          <template v-slot:actions>
            <v-icon color="white"> mdi-chevron-up </v-icon>
          </template>
        </v-expansion-panel-header>
        <v-expansion-panel-content>
          <div class="mx-n6 mb-n4" v-if="celeryProgressByUser">
            <task-list-item
              v-for="task in celeryProgressByUser"
              :task="task"
              :key="task.meta.taskId"
            />
          </div>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </v-bottom-sheet>
</template>

<script>
import TaskListItem from "./TaskListItem.vue";
import gqlCeleryProgressButton from "./celeryProgressBottom.graphql";

export default {
  name: "CeleryProgressBottom",
  components: { TaskListItem },
  data() {
    return { open: 0 };
  },
  mounted() {
    // Vuetify uses the hideScroll method to disable scrolling by setting an event listener
    // to the window. As event listeners can only be removed by referencing the listener
    // method and because vuetify this method is called on every state change of the dialog,
    // we simply replace the method in this component instance
    this.$refs.sheet.hideScroll = this.$refs.sheet.showScroll;
  },
  computed: {
    show() {
      return this.celeryProgressByUser && this.celeryProgressByUser.length > 0;
    },
    numberOfTasks() {
      if (!this.celeryProgressByUser) {
        return 0;
      }
      return this.celeryProgressByUser.length;
    },
  },
  apollo: {
    celeryProgressByUser: {
      query: gqlCeleryProgressButton,
      pollInterval: 30000,
    },
  },
};
</script>
