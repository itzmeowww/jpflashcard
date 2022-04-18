<script>
  export let settings;
  import { slide } from "svelte/transition";

  const setBatchSize = (x) => {
    settings.batchSize = x;
  };
</script>

<div
  transition:slide
  class=" fixed z-30 h-screen w-full bg-white text-sm top-0 text-black flex justify-center items-center px-4"
>
  <div class="w-full max-w-md">
    <h1 class="w-full text-center border-b pb-1 mb-6 text-xl mx-auto font-mono">
      Settings
    </h1>
    <div class="w-full flex flex-col gap-2 justify-center items-center">
      <div class="flex">
        <h1>Word Size :</h1>
        {#each [40] as x}
          {#if x == settings.batchSize}
            <button class="bg-black text-white px-1 border rounded">{x}</button>
          {:else}
            <button on:click={() => setBatchSize(x)} class="px-1 border rounded"
              >{x}</button
            >
          {/if}
        {/each}
      </div>
      <div class="flex">
        <label for="" class="mr-2">Hide Credit</label>
        <input
          type="checkbox"
          bind:checked={settings.hideCredit}
          name=""
          id=""
        />
      </div>
      <!-- <div class="flex">
        <label for="" class="mr-2">Reverse</label>
        <input type="checkbox" bind:checked={settings.reversed} name="" id="" />
      </div> -->
      <div class="flex items-center">
        <label for="" class="mr-2">Show Meaning Before Hiding Word</label>
        <input
          type="checkbox"
          bind:checked={settings.showMeaningBeforeHide}
          name=""
          id=""
        />
      </div>
      <div class="flex items-center">
        <label for="" class="mr-2">Show Meaning Before Prev/Next Word</label>
        <input
          type="checkbox"
          bind:checked={settings.showMeaningBeforeChange}
          name=""
          id=""
        />
      </div>
    </div>
  </div>
</div>
