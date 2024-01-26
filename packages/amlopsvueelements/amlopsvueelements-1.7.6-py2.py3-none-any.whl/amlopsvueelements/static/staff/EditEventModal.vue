<script setup lang="ts">
import { computed, nextTick, reactive, ref, watch } from 'vue'
// @ts-ignore
import { useVuelidate } from '@vuelidate/core'
import { required, requiredIf, requiredUnless } from '@vuelidate/validators'
import type { AxiosError } from 'axios'
import moment from 'moment-timezone'
import { useMutation } from '@tanstack/vue-query'

import {
  BAlert,
  BButton,
  BForm,
  BFormGroup,
  BFormInvalidFeedback,
  BFormTextarea,
  BModal
} from 'bootstrap-vue-next'
import { FlatPickr, SelectField } from 'shared/components'
import ApplyDatesSelect from '@/components/common/ApplyDatesSelect.vue'

import type { EventApi } from '@fullcalendar/core'
import type { Person } from '@/models/Person'
import type {
  SpecificEntryPayload,
  SpecificEntryPersonPopulated,
  BlanketEntryPersonPopulated,
  BlanketEntryPayload
} from '@/models/Entry'
import type { EntryType } from '@/models/EntryType'
import { usePeople } from '@/composables/usePeople'
import { useEntryTypes } from '@/composables/useEntryTypes'

import entryService from '@/services/EntryService'

import ApplyDaysSelect from '@/components/common/ApplyDaysSelect.vue'
import ApplyWeeksSelect from '@/components/common/ApplyWeeksSelect.vue'
import ConfirmModal, { type ConfirmOption } from '@/components/calendar/ConfirmModal.vue'

export type EventEditMode = 'add-blanket' | 'add-specific' | 'quick-add-sickness-absence' | 'edit'

interface Props {
  mode?: EventEditMode
  event?: EventApi
}

interface FormValues {
  id: number | undefined
  person: Person | undefined
  start_hour: string | undefined
  end_hour: string | undefined
  comment: string | undefined
  start_date: string | undefined
  end_date: string | undefined
  replaces_other_entry: number | undefined
  replaces_own_entry: number | undefined
  applied_on_dates: number[] | undefined
  applied_on_days: number[] | undefined
  applied_on_weeks: number[] | undefined
  entry_type: EntryType | undefined
}

const defaultValues: FormValues = {
  id: undefined,
  person: undefined,
  start_hour: '',
  end_hour: '',
  comment: undefined,
  start_date: '',
  end_date: '',
  replaces_other_entry: undefined,
  replaces_own_entry: undefined,
  applied_on_dates: undefined,
  applied_on_days: undefined,
  applied_on_weeks: [0],
  entry_type: undefined
}

const open = defineModel<boolean>('open')
const props = withDefaults(defineProps<Props>(), {
  mode: 'add-specific'
})
const emit = defineEmits(['event-created', 'hide'])

const { data: people, isLoading: isLoadingPeople } = usePeople()
const { data: entryTypes, isLoading: isLoadingEntryTypes } = useEntryTypes()

const isDelete = ref<boolean>(false)
const isConfirmModalOpen = ref<boolean>(false)

const isBlanketEntry = computed(() => {
  switch (props.mode) {
    case 'add-specific':
    case 'quick-add-sickness-absence':
      return false
    case 'add-blanket':
      return true
    case 'edit':
    default:
      return props.event?.id.startsWith('blanket') ?? false
  }
})
const entry = computed<SpecificEntryPersonPopulated | BlanketEntryPersonPopulated>(
  () => props.event?.extendedProps as SpecificEntryPersonPopulated | BlanketEntryPersonPopulated
)

const { isPending, mutate } = useMutation({
  mutationFn: ({
    entries,
    isDelete
  }: {
    entries: SpecificEntryPayload[] | BlanketEntryPayload[]
    isDelete?: boolean
  }) =>
    isBlanketEntry.value
      ? isDelete
        ? entryService.deleteBlanketEntries(entries)
        : props.mode === 'edit'
          ? entryService.updateBlanketEntries(entries)
          : entryService.createBlanketEntries(entries)
      : isDelete
        ? entryService.deleteSpecificEntries(entries)
        : props.mode === 'edit'
          ? entryService.updateSpecificEntries(entries)
          : entryService.createSpecificEntries(entries),
  onSuccess: (data) => {
    emit('event-created', data)
    open.value = false
  },
  onError: (error: AxiosError) => {
    if (!error.response) {
      non_field_errors.value = ['Network error']
      return
    }

    const errors = (error.response.data as any).errors
      ? (error.response.data as any).errors[0]
      : undefined
    if (!errors) {
      non_field_errors.value = ['Unknown error']
    } else if (errors.non_field_errors) {
      non_field_errors.value = errors.non_field_errors
    } else if (errors.message) {
      non_field_errors.value = [errors.message]
    } else {
      $externalResults.value = errors
    }
  }
})

const non_field_errors = ref<string[]>([])
const $externalResults = ref({})
const rules = computed(() => ({
  id: {},
  person: { required },
  start_hour: { requiredUnless: requiredUnless(values.entry_type?.requires_full_workday ?? false) },
  end_hour: { requiredUnless: requiredUnless(values.entry_type?.requires_full_workday ?? false) },
  comment: { requiredIf: requiredIf(values.entry_type?.requires_comment ?? false) },
  start_date: { required },
  end_date: { required },
  replaces_other_entry: {},
  replaces_own_entry: {},
  applied_on_dates: {},
  // applied_on_dates: { requiredUnless: requiredUnless(isBlanketEntry) },
  applied_on_days: { requiredIf: requiredIf(isBlanketEntry) },
  applied_on_weeks: { requiredIf: requiredIf(isBlanketEntry) },
  entry_type: { required }
}))
const values = reactive<FormValues>({
  id: defaultValues.id,
  person: defaultValues.person,
  start_hour: defaultValues.start_hour,
  end_hour: defaultValues.end_hour,
  comment: defaultValues.comment,
  start_date: defaultValues.start_date,
  end_date: defaultValues.end_date,
  replaces_other_entry: defaultValues.replaces_other_entry,
  replaces_own_entry: defaultValues.replaces_own_entry,
  applied_on_dates: defaultValues.applied_on_dates,
  applied_on_days: defaultValues.applied_on_days,
  applied_on_weeks: defaultValues.applied_on_weeks,
  entry_type: defaultValues.entry_type
})
const v$ = useVuelidate(rules, values, { $externalResults, $autoDirty: true })

const modalTitle = computed(() => {
  return props.mode === 'quick-add-sickness-absence'
    ? 'Quick-Add Sickness Absence'
    : (props.mode === 'edit' ? 'Edit ' : 'Add ') +
        (isBlanketEntry.value ? 'Schedule Event' : 'Calendar Event')
})

const timePeriodDescription = computed(() => {
  const timezoneOfSelectedPerson = values.person?.timezone
  const start_hour_utc = values.start_hour
    ? moment()
        .startOf('day')
        .add(values.start_hour)
        .tz(timezoneOfSelectedPerson ?? 'utc')
    : undefined
  const end_hour_utc = values.end_hour
    ? moment()
        .startOf('day')
        .add(values.end_hour)
        .tz(timezoneOfSelectedPerson ?? 'utc')
    : undefined

  return start_hour_utc || end_hour_utc
    ? `${
        start_hour_utc ? start_hour_utc.format(`(HH:mm ${timezoneOfSelectedPerson ?? 'UTC'})`) : ''
      } - ${
        end_hour_utc ? end_hour_utc.format(`(HH:mm ${timezoneOfSelectedPerson ?? 'UTC'})`) : ''
      }`
    : ''
})

const selectAppliedOnWeeks = (action: ConfirmOption) => {
  // The week number starting from start_date of event
  let weekno = 0
  for (
    const iDate = moment(values?.start_date).startOf('week');
    iDate.isSameOrBefore(props.event?.start);
    iDate.add(1, 'week')
  ) {
    weekno++
  }
  let weeks: number[]
  if (action === 'only') {
    weeks = [weekno]
  } else if (action === 'following') {
    const index = values?.applied_on_weeks?.indexOf(weekno)
    weeks = values.applied_on_weeks?.slice(index) ?? []
  } else {
    weeks = values.applied_on_weeks ?? []
  }
  return weeks
}

const selectAppliedOnDates = (action?: ConfirmOption) => {
  const date = moment(props.event?.start).get('date')

  let dates: number[]
  if (action === 'only') {
    dates = [date]
  } else if (action === 'following') {
    const index = values.applied_on_dates?.indexOf(date)
    dates = values.applied_on_dates?.slice(index) ?? []
  } else {
    dates = values.applied_on_dates ?? []
  }

  return dates
}

const onConfirm = (action: ConfirmOption) => {
  const entryPayload: SpecificEntryPayload | BlanketEntryPayload = {
    id: values.id,
    person: values.person?.person_id,
    team: values.person?.aml_team_id,
    // Transform local time to UTC
    start_hour: values.entry_type?.requires_full_workday
      ? '00:00:00'
      : moment().startOf('day').add(values.start_hour).tz('utc').format('HH:mm:ss'),
    end_hour: values.entry_type?.requires_full_workday
      ? '23:59:59'
      : moment().startOf('day').add(values.end_hour).tz('utc').format('HH:mm:ss'),
    comment: values.comment,
    start_date: values.start_date,
    end_date: values.end_date,
    entry_type: values.entry_type?.id,
    ...(isBlanketEntry.value
      ? {
          applied_on_days: values.applied_on_days,
          applied_on_weeks: values.applied_on_weeks
        }
      : {
          applied_on_dates: values.applied_on_dates
        })
  }

  if (props.mode === 'edit') {
    entryPayload.flagged_for_edit = entry.value?.flagged_for_edit
    entryPayload.flagged_for_delete = entry.value?.flagged_for_delete
    if (isDelete.value) {
      entryPayload.flagged_for_delete = true
    } else {
      entryPayload.flagged_for_edit = true
    }

    if (isBlanketEntry.value) {
      if ('applied_on_weeks' in entryPayload) {
        entryPayload.applied_on_weeks = selectAppliedOnWeeks(action)
      }
    } else {
      if ('applied_on_dates' in entryPayload) {
        entryPayload.applied_on_dates = selectAppliedOnDates(action)
      }
    }
  } else {
    if (!isBlanketEntry.value && values.start_date && values.end_date) {
      const availableDates: number[] = []
      for (
        const iDate = moment(values.start_date);
        iDate.isSameOrBefore(values.end_date);
        iDate.add(1, 'day')
      ) {
        if (availableDates.length === 31) {
          break
        }

        const date = iDate.get('date')
        if (availableDates.includes(date)) {
          continue
        }
        availableDates.push(date)
      }
      availableDates.sort((a, b) => a - b)
      if ('applied_on_dates' in entryPayload) {
        entryPayload.applied_on_dates = availableDates
      }
    }
  }
  mutate({ entries: [entryPayload], isDelete: isDelete.value })
}

const onSubmit = async () => {
  const isValid = await v$?.value?.$validate()
  non_field_errors.value = []

  if (!isValid) {
    return
  }

  isDelete.value = false
  if (props.mode === 'edit') {
    isConfirmModalOpen.value = true
  } else {
    onConfirm('all')
  }
}

const onCancel = () => {
  open.value = false
}

const onDelete = () => {
  isDelete.value = true
  isConfirmModalOpen.value = true
}

const resetForm = async () => {
  if (entry.value) {
    values.id = entry.value.id
    values.person = entry.value.person
    // Transform UTC time to local time
    values.start_hour = moment
      .utc()
      .startOf('day')
      .add(entry.value.start_hour)
      .tz(entry.value.person.timezone ?? moment.tz.guess())
      .format('HH:mm:ss')
    values.comment = entry.value.comment
    values.start_date = entry.value.start_date
    values.entry_type = entry.value.entry_type
    // Wait until start time and start date field updated
    await nextTick()
    // Transform UTC time to local time
    values.end_hour = moment
      .utc()
      .startOf('day')
      .add(entry.value.end_hour)
      .tz(entry.value.person.timezone ?? moment.tz.guess())
      .format('HH:mm:ss')
    values.end_date = entry.value.end_date

    if (isBlanketEntry.value) {
      values.applied_on_days = (entry.value as BlanketEntryPersonPopulated)?.applied_on_days
      values.applied_on_weeks = (entry.value as BlanketEntryPersonPopulated)?.applied_on_weeks
    } else {
      values.applied_on_dates = (entry.value as SpecificEntryPersonPopulated)?.applied_on_dates
    }
  } else {
    values.id = defaultValues.id
    values.person = defaultValues.person
    values.start_hour = defaultValues.start_hour
    values.end_hour = defaultValues.end_hour
    values.comment = defaultValues.comment
    values.start_date = defaultValues.start_date
    values.end_date = defaultValues.end_date
    values.replaces_other_entry = defaultValues.replaces_other_entry
    values.replaces_own_entry = defaultValues.replaces_own_entry
    values.applied_on_dates = defaultValues.applied_on_dates
    values.applied_on_days = defaultValues.applied_on_days
    values.applied_on_weeks = defaultValues.applied_on_weeks
    values.entry_type = defaultValues.entry_type
  }

  $externalResults.value = {}
  v$.value.$reset()
}

watch(values, () => {
  non_field_errors.value = []
})
watch(open, () => {
  if (open.value) {
    resetForm()
  }
})
watch(props, () => {
  if (props.mode === 'quick-add-sickness-absence') {
    values.start_date = moment.utc().format('YYYY-MM-DD')
  }
})
watch([entryTypes, props], () => {
  if (props.mode === 'quick-add-sickness-absence' && entryTypes.value) {
    values.entry_type = entryTypes.value.find((entryType) => entryType.name === 'Sick Absence')
  }
})
</script>

<template>
  <BModal
    v-model="open"
    :no-close-on-backdrop="isPending"
    :title="modalTitle"
    centered
    @hide="emit('hide')"
  >
    <BForm>
      <BAlert
        :model-value="true"
        variant="danger"
        class="mb-[1rem]"
        v-for="error of non_field_errors"
        :key="error"
        >{{ error }}</BAlert
      >

      <BFormGroup label="Team Member:" class="mb-[1rem]" :state="!v$.person.$error">
        <SelectField
          :loading="isLoadingPeople"
          :options="people"
          label="name"
          v-model="values.person"
          required
          :clearable="false"
          :append-to-body="false"
          placeholder="Please select Team Member"
          class="mb-0"
        />
        <BFormInvalidFeedback :state="!v$.person.$error">
          <div v-for="error of v$.person.$errors" :key="error.$uid">{{ error.$message }}</div>
        </BFormInvalidFeedback>
      </BFormGroup>
      <BFormGroup
        label="Start & End Time (Local):"
        class="mb-[1rem]"
        :state="v$.start_hour.$error || v$.end_hour.$error"
        v-if="mode !== 'quick-add-sickness-absence'"
      >
        <div v-if="values.entry_type?.requires_full_workday" class="all-day form-control">
          All Day
        </div>
        <div class="flex align-items-center gap-x-2" v-else>
          <FlatPickr
            :config="{
              noCalendar: true,
              enableTime: true,
              dateFormat: 'H:i',
              time_24hr: true,
              allowInput: true,
              altInput: true,
              altFormat: 'H:i'
            }"
            v-model="values.start_hour"
            placeholder="Start Time"
          />
          <span> - </span>
          <FlatPickr
            :config="{
              noCalendar: true,
              enableTime: true,
              dateFormat: 'H:i',
              time_24hr: true,
              position: 'auto right',
              minTime: values.start_hour,
              allowInput: true,
              altInput: true,
              altFormat: 'H:i'
            }"
            v-model="values.end_hour"
            placeholder="End Time"
          />
        </div>
        <small class="text-body-secondary form-text italic">
          {{ values.entry_type?.requires_full_workday ? '' : timePeriodDescription }}
        </small>
        <BFormInvalidFeedback :state="!v$.start_hour.$error">
          <div v-for="error of v$.start_hour.$errors" :key="error.$uid">
            {{ error.$message }}
          </div>
        </BFormInvalidFeedback>
        <BFormInvalidFeedback :state="!v$.end_hour.$error">
          <div v-for="error of v$.end_hour.$errors" :key="error.$uid">
            {{ error.$message }}
          </div>
        </BFormInvalidFeedback>
      </BFormGroup>
      <BFormGroup
        :label="mode === 'quick-add-sickness-absence' ? 'Reason for Sickness Absence:' : 'Comment:'"
        class="mb-[1rem]"
        :state="!v$.comment.$error"
      >
        <BFormTextarea v-model="values.comment" rows="3" max-rows="6" />
        <BFormInvalidFeedback :state="!v$.comment.$error">
          <div v-for="error of v$.comment.$errors" :key="error.$uid">
            {{ error.$message }}
          </div>
        </BFormInvalidFeedback>
      </BFormGroup>
      <BFormGroup
        label="Start & End Date:"
        class="mb-[1rem]"
        :state="v$.start_date.$error || v$.end_date.$error"
      >
        <div class="flex align-items-center gap-x-2">
          <FlatPickr
            :config="{
              allowInput: true,
              altInput: true,
              altFormat: 'Y-m-d',
              locale: { firstDayOfWeek: 1 }
            }"
            v-model="values.start_date"
            placeholder="Start Date"
            :disabled="mode === 'edit'"
          />
          <span> - </span>
          <FlatPickr
            :config="{
              minDate: values.start_date,
              allowInput: true,
              altInput: true,
              altFormat: 'Y-m-d',
              locale: { firstDayOfWeek: 1 }
            }"
            v-model="values.end_date"
            placeholder="End Date"
            :disabled="mode === 'edit'"
          />
        </div>
        <BFormInvalidFeedback :state="!v$.start_date.$error">
          <div v-for="error of v$.start_date.$errors" :key="error.$uid">
            {{ error.$message }}
          </div>
        </BFormInvalidFeedback>
        <BFormInvalidFeedback :state="!v$.end_date.$error">
          <div v-for="error of v$.end_date.$errors" :key="error.$uid">
            {{ error.$message }}
          </div>
        </BFormInvalidFeedback>
      </BFormGroup>
      <BFormGroup
        label="Applicable Dates:"
        class="mb-[1rem] hidden"
        :state="v$.applied_on_dates.$error"
        v-if="!isBlanketEntry"
      >
        <ApplyDatesSelect
          v-model="values.applied_on_dates"
          :start_date="values.start_date"
          :end_date="values.end_date"
          :disabled="mode === 'edit' || !values.start_date || !values.end_date"
          placeholder="Please select Applicable Dates"
        />
        <BFormInvalidFeedback :state="!v$.applied_on_dates.$error">
          <div v-for="error of v$.applied_on_dates.$errors" :key="error.$uid">
            {{ error.$message }}
          </div>
        </BFormInvalidFeedback>
      </BFormGroup>
      <template v-else>
        <BFormGroup label="Applicable Days:" class="mb-[1rem]" :state="v$.applied_on_days.$error">
          <ApplyDaysSelect
            v-model="values.applied_on_days"
            :disabled="mode === 'edit' || !values.start_date || !values.end_date"
          />
          <BFormInvalidFeedback :state="!v$.applied_on_days.$error">
            <div v-for="error of v$.applied_on_days.$errors" :key="error.$uid">
              {{ error.$message }}
            </div>
          </BFormInvalidFeedback>
        </BFormGroup>
        <BFormGroup label="Applicable Weeks:" class="mb-[1rem]" :state="v$.applied_on_weeks.$error">
          <ApplyWeeksSelect
            v-model="values.applied_on_weeks"
            :start_date="values.start_date"
            :end_date="values.end_date"
            :disabled="mode === 'edit' || !values.start_date || !values.end_date"
            placeholder="Please select Applicable Weeks"
          />
          <BFormInvalidFeedback :state="!v$.applied_on_weeks.$error">
            <div v-for="error of v$.applied_on_weeks.$errors" :key="error.$uid">
              {{ error.$message }}
            </div>
          </BFormInvalidFeedback>
        </BFormGroup>
      </template>
      <BFormGroup
        label="Event Type:"
        class="mb-[1rem]"
        :state="v$.entry_type.$error"
        v-if="mode !== 'quick-add-sickness-absence'"
      >
        <SelectField
          :loading="isLoadingEntryTypes"
          :options="entryTypes"
          label="name"
          v-model="values.entry_type"
          :clearable="false"
          :append-to-body="false"
          placeholder="Please select Event Type"
          class="mb-0"
        />
        <BFormInvalidFeedback :state="!v$.entry_type.$error">
          <div v-for="error of v$.entry_type.$errors" :key="error.$uid">{{ error.$message }}</div>
        </BFormInvalidFeedback>
      </BFormGroup>
    </BForm>

    <template v-slot:ok>
      <BButton type="submit" :disabled="isPending" variant="primary" @click="onSubmit">
        {{ mode === 'edit' ? 'Update' : 'Submit' }}
      </BButton>
    </template>
    <template v-slot:cancel>
      <BButton type="button" variant="danger" @click="onDelete" v-if="mode === 'edit'">
        Delete
      </BButton>
      <BButton type="button" @click="onCancel" v-else>Cancel</BButton>
    </template>
  </BModal>

  <ConfirmModal
    v-model:open="isConfirmModalOpen"
    :is-delete="isDelete"
    :is-blanket-entry="isBlanketEntry"
    @confirm="onConfirm"
  />
</template>

<style scoped lang="scss"></style>
