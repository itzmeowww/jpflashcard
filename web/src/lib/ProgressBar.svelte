<script>
  export let startIdx = 0;
  export let progress = 0;
  export let endIdx = 0;
</script>

<section>
  <div class=" w-48 flex items-center justify-center gap-2">
    <h1 class="text-xs">{startIdx}</h1>
    <progress value={progress} class="w-64 h-0.5 flex-1" />
    <h1 class="text-xs">{endIdx}</h1>
  </div>
</section>
