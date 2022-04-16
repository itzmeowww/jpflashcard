<script>
  export let completed, num, showMeaning;
  const setHideMeaning = () => {
    showMeaning = false;
  };
  const setShowMeaning = () => {
    showMeaning = true;
  };
</script>

<div
  class="relative w-64 h-40 rounded-lg shadow-md bg-white flex  justify-center items-center overflow-hidden cursor-pointer select-none touch-none"
>
  <div
    class="left-2 top-2 absolute w-7 h-7 border rounded-full flex items-center justify-center"
  >
    <h1 class="text-xs">{num}</h1>
  </div>
  {#if completed}
    <div
      on:click={setHideMeaning}
      class={`bg-black text-white absolute w-full h-full flex-col justify-center items-center py-4 gap-2 transition-all flex px-4 text-center`}
    >
      <h1 class="text-md font-light font-mono">Completed</h1>
    </div>
  {:else if showMeaning}
    <div
      on:click={setHideMeaning}
      class={`absolute w-full h-full flex-col justify-center items-center py-4 gap-2 transition-all flex px-4 text-center`}
    >
      <slot name="meaning" />
    </div>
  {:else}
    <div
      on:click={setShowMeaning}
      class={`absolute w-full h-full flex-col justify-center items-center py-4 gap-2 flex`}
    >
      <slot name="word" />
    </div>
  {/if}
</div>
