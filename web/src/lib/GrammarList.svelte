<script>
  export let selecting;
  import { fade } from "svelte/transition";
  import lessons from "../data/jplang_grammar";

  let checked = {};
</script>

<section transition:fade>
  <div class="flex flex-col w-full gap-4 items-center justify-center py-12">
    <button
      on:click={() => {
        selecting = true;
      }}
      class="fixed top-4 underline font-mono">go back</button
    >
    {#each Object.entries(lessons) as [key, lesson]}
      <div class="border rounded-lg shadow p-4 flex flex-col gap-2 bg-white">
        <h1
          class="border border-black rounded-full w-6 h-6 flex items-center justify-center text-xs font-mono mx-auto"
        >
          {key}
        </h1>
        {#each lesson as grammar}
          <div class="flex gap-3 items-center justify-start w-64">
            <h1 class="bg-black text-white rounded text-xs pr-1 w-8 text-right">
              {grammar.split(" ")[0].split("-").splice(1).join(".")}
            </h1>
            <input
              type="checkbox"
              name=""
              id={grammar.split(" ")[0]}
              bind:checked={checked[grammar.split(" ")[0]]}
              class="w-4"
            />
            <label
              for={grammar.split(" ")[0]}
              class={`w-full text-sm  break-all ${
                checked[grammar.split(" ")[0]] && "line-through"
              }`}
            >
              {grammar.split(" ")[1]}
            </label>
          </div>
        {/each}
      </div>
    {/each}
  </div>
</section>
