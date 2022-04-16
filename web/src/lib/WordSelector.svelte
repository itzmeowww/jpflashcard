<script>
  export let groups, currentWordSet, currentBatch, words, wordId, showMeaning;
  export let status;
  export let parentSetCurrentBatch;

  const setHideMeaning = () => {
    showMeaning = false;
  };

  const setCurrentWordSet = (x) => {
    if (x == currentWordSet) return;
    currentWordSet = x;
    setHideMeaning();
    if (currentBatch != 0) currentBatch = 0;
    wordId = words[x].lastIdx;
  };

  const setCurrentBatch = (x) => {
    setHideMeaning();
    parentSetCurrentBatch(x);
  };
</script>

<div class="w-64 px-2 flex justify-between items-center touch-none">
  {#each groups as group}
    <button
      on:click={() => {
        setCurrentWordSet(group);
      }}
      class={`${
        currentWordSet == group ? "bg-black text-white" : "bg-white"
      } w-10 shadow-md rounded-md font-mono touch-none`}
    >
      {group}
    </button>
  {/each}
</div>

<div class="w-64 grid px-2 grid-cols-5 gap-2 border-t py-2">
  {#each status[currentWordSet].batches as batchInfo, i}
    <button
      on:click={() => {
        setCurrentBatch(i);
      }}
      class={`${
        currentBatch == i ? "bg-black text-white" : "bg-white"
      } w-10 shadow-md rounded-md font-mono touch-none text-sm`}>{i + 1}</button
    >
  {/each}
</div>
