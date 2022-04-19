<script>
  export let selecting;
  import lessons from "../data/jplang_grammar";
  console.log(lessons[1][2].split(" ")[0].split("-"));
</script>

<section>
  <div class="flex flex-col w-full gap-4 items-center justify-center py-12">
    <button
      on:click={() => {
        selecting = true;
      }}
      class="fixed top-4 underline font-mono">go back</button
    >
    {#each Object.entries(lessons) as [key, lesson]}
      <div class="border rounded-lg shadow p-4 flex flex-col gap-2">
        <h1
          class="border border-black rounded-full w-6 h-6 flex items-center justify-center text-xs font-mono"
        >
          {key}
        </h1>
        {#each lesson as grammar}
          <div class="flex gap-2 items-center justify-start w-64">
            <h1
              class="bg-black text-white rounded text-xs pl-1 w-12 text-start"
            >
              {grammar.split(" ")[0]}
            </h1>
            <h1 class="text-sm">{grammar.split(" ")[1]}</h1>
          </div>
        {/each}
      </div>
    {/each}
  </div>
</section>
