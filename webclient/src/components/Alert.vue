<template>
    <div>
        <b-alert variant="success" show>
            {{ response }}
        </b-alert>
    </div>
</template>
<script>
export default {
  props: ['response'],
};
</script>
