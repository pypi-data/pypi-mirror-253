<script setup lang="ts">
import { ref, reactive, watchEffect, watch, nextTick } from 'vue'

import moment from 'moment-timezone'
import type { CalendarOptions, EventApi, EventClickArg } from '@fullcalendar/core'
import FullCalendar from '@fullcalendar/vue3'
import bootstrap5Plugin from '@fullcalendar/bootstrap5'
import resourceTimelinePlugin from '@fullcalendar/resource-timeline'
import rrulePlugin from '@fullcalendar/rrule'
import momentPlugin from '@fullcalendar/moment'
import momentTimezone from '@fullcalendar/moment-timezone'
import interactionPlugin from '@fullcalendar/interaction'

import { BOverlay, BDropdown, BDropdownItem } from 'bootstrap-vue-next'
import EditEventModal, { type EventEditMode } from '@/components/calendar/EditEventModal.vue'
import { SelectField } from 'shared/components'

import type { Team } from '@/models/Team'
import eventService from '@/services/EventService'
import { useTimezones } from '@/composables/useTimezones'
import { useTeams } from '@/composables/useTeams'

const calendar = ref()
const isCalendarMounted = ref(false)
const isEditEventModalOpen = ref(false)
const isLoading = ref(false)
const selectedTimezone = ref({
  label: 'UTC',
  value: 'UTC'
})
const selectedTeams = ref<Team[]>([])
const clickedEvent = ref<EventApi | undefined>(undefined)
const eventEditMode = ref<EventEditMode>('add-specific')
const isAddButtonDropdownShow = ref<boolean>(false)

const { data: timezones, isLoading: isLoadingTimezones } = useTimezones()
const { data: teams, isLoading: isLoadingTeams } = useTeams()

const calendarOptions = reactive<CalendarOptions>({
  plugins: [
    bootstrap5Plugin,
    resourceTimelinePlugin,
    rrulePlugin,
    momentPlugin,
    momentTimezone,
    interactionPlugin
  ],
  schedulerLicenseKey: 'CC-Attribution-NonCommercial-NoDerivatives',
  themeSystem: 'bootstrap5',
  initialView: 'resourceTimelineDay',
  height: '100%',
  customButtons: {
    quickAddSicknessAbsence: {
      text: 'Quick-Add Sickness Absence',
      click() {
        handleQuickAddSicknessAbsence()
      }
    },
    timezoneSelector: {
      text: ''
    },
    add: {
      text: ''
    }
  },
  headerToolbar: {
    right:
      'timezoneSelector add quickAddSicknessAbsence resourceTimelineMonth,resourceTimelineWeek,resourceTimelineDay prev,today,next'
  },
  resourceAreaHeaderClassNames: 'custom-resource-area-header',
  resourceGroupField: 'groupId',
  resourceLabelClassNames: 'centered-resource-label',
  resources: [],
  events: (info, successCallback, failureCallback) => {
    const selectedTeamNames = selectedTeams.value?.map((team) => team.name)
    eventService
      .fetchEvents(info.start, info.end, selectedTeamNames)
      .then(({ events, resources }) => {
        successCallback(events)
        calendarOptions.resources = resources
      })
      .catch(failureCallback)
  },
  views: {
    resourceTimelineMonth: {
      slotLabelFormat: 'D (dd)'
    },
    resourceTimelineWeek: {
      slotLabelFormat: ['ddd M/D', 'HH:mm']
    },
    resourceTimelineDay: {
      slotLabelFormat: ['HH:mm']
    }
  },
  selectable: true,
  selectMirror: true,
  firstDay: 1,
  viewDidMount: () => {
    // Patch the vue target for teleporting vue component in header toolbar

    const timezoneSelectorButton = document.querySelector(
      '.fc-header-toolbar button.fc-timezoneSelector-button'
    )
    timezoneSelectorButton?.setAttribute('style', 'display: none;')
    const timezoneSelectTarget = document.createElement('div')
    timezoneSelectTarget.id = 'timezone-select-target'
    timezoneSelectorButton?.replaceWith(timezoneSelectorButton, timezoneSelectTarget)

    const addButton = document.querySelector('.fc-header-toolbar button.fc-add-button')
    addButton?.setAttribute('style', 'display: none;')
    const addEventButtonTarget = document.createElement('div')
    addEventButtonTarget.id = 'add-event-button-target'
    addButton?.replaceWith(addButton, addEventButtonTarget)

    isCalendarMounted.value = true
  },
  loading: (loading) => {
    isLoading.value = loading
  },
  eventClick: (eventClickInfo: EventClickArg) => {
    const { event } = eventClickInfo
    handleEventEdit(event, 'edit')
  }
})

const refetchEvents = () => {
  const calendarApi = calendar.value?.getApi()
  calendarApi && calendarApi.refetchEvents()
}

const handleEventEdit = async (event?: EventApi, editMode?: EventEditMode) => {
  if (!editMode) {
    editMode = 'add-specific'
  }

  clickedEvent.value = event
  eventEditMode.value = editMode
  await nextTick()
  isEditEventModalOpen.value = true
}

const handleQuickAddSicknessAbsence = () => {
  handleEventEdit(undefined, 'quick-add-sickness-absence')
}

watch([selectedTeams], () => {
  refetchEvents()
})
watchEffect(() => {
  calendarOptions.timeZone = selectedTimezone.value.value
})
</script>
<template>
  <div class="h-full">
    <BOverlay :show="isLoading" rounded="sm" class="h-full">
      <FullCalendar ref="calendar" :options="calendarOptions">
        <template v-slot:resourceAreaHeaderContent>
          <SelectField
            :options="teams"
            label="name"
            :loading="isLoadingTeams"
            v-model="selectedTeams"
            multiple
            :taggable="true"
            placeholder="Please select Teams"
            class="mb-0"
          />
        </template>
        <template v-slot:eventContent="arg">
          <div class="text-center">
            <b>{{ arg.event.title }}</b>
            <div v-if="arg.view.type !== 'resourceTimelineMonth'">
              <template v-if="arg.event.allDay"> All Day </template>
              <template v-else>
                {{
                  moment(arg.event.start)
                    .tz(
                      selectedTimezone.value === 'local'
                        ? moment.tz.guess()
                        : selectedTimezone.value
                    )
                    .format('HH:mm')
                }}
                -
                {{
                  moment(arg.event.end)
                    .tz(
                      selectedTimezone.value === 'local'
                        ? moment.tz.guess()
                        : selectedTimezone.value
                    )
                    .format('HH:mm')
                }}
                {{ selectedTimezone.label }}
                (
                {{ moment.duration(arg.event.end).subtract(arg.event.start).hours() }}h
                {{ moment.duration(arg.event.end).subtract(arg.event.start).minutes() }}m )
              </template>
            </div>
          </div>
        </template>
        <template v-slot:resourceLabelContent="arg">
          <div class="text-center">
            <b>{{ arg.resource.title }}</b>
            <div>({{ arg.resource.extendedProps.role }})</div>
          </div>
        </template>
      </FullCalendar>
    </BOverlay>
    <Teleport to="#timezone-select-target" v-if="isCalendarMounted">
      <div class="flex align-items-center gap-2">
        <span>Timezone: </span>
        <div class="timezone-select-container">
          <SelectField
            :options="timezones"
            label="label"
            :loading="isLoadingTimezones"
            v-model="selectedTimezone"
            :clearable="false"
            :append-to-body="false"
            placeholder="Please select Timezone"
            class="mb-0"
          />
        </div>
      </div>
    </Teleport>
    <Teleport to="#add-event-button-target" v-if="isCalendarMounted">
      <BDropdown
        v-model="isAddButtonDropdownShow"
        split
        end
        text="Add Calendar Event"
        variant="primary"
        @click="handleEventEdit()"
      >
        <BDropdownItem variant="primary" @click="handleEventEdit(undefined, 'add-blanket')">
          Add Schedule Event
        </BDropdownItem>
      </BDropdown>
    </Teleport>

    <EditEventModal
      v-model:open="isEditEventModalOpen"
      :event="clickedEvent"
      :mode="eventEditMode"
      @event-created="refetchEvents()"
    />
  </div>
</template>

<style scoped lang="scss">
.timezone-select-container {
  width: 220px;
}
</style>
