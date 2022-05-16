<template>
<div class="container">
	<div id="calendar">
		<h1>My Calendar</h1>
		<calendar-view
			:show-date="showDate"
			class="theme-default holiday-us-traditional holiday-us-official">
			<template #header="{ headerProps }">
				<calendar-view-header
					:header-props="headerProps"
					@input="setShowDate" />
			</template>
		</calendar-view>
	</div>
</div>
</template>
<script>
	import { CalendarView, CalendarViewHeader } from "vue-simple-calendar"
  import "vue-simple-calendar/dist/style.css"

	export default {
		name: 'calendar',
		data: function() {
			return { showDate: new Date() }
		},
		components: {
			CalendarView,
			CalendarViewHeader,
		},
		methods: {
			setShowDate(d) {
				this.showDate = d;
			},
		}
	}
</script>
<style>
.container {
  padding-top: 1.5rem;
  height: 29rem;
}
#calendar {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  color: #2c3e50;
  height: 67vh;
  width: 90vw;
  margin-left: auto;
  margin-right: auto;
}
</style>