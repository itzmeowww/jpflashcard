<script>
  import ProgressBar from "./ProgressBar.svelte";
  export let startIdx, endIdx, progress;
  export let status, completed, currentWordSet, wordId;
  export let showMeaning;
  const setHideMeaning = () => {
    showMeaning = false;
  };
  const prevWord = () => {
    let newWordId = wordId - 1;
    // console.log(newWordId);
    if (newWordId < startIdx) newWordId = endIdx;
    // console.log(currentWordSet, startIdx, endIdx, wordId);
    while (status[currentWordSet].list[newWordId] === true) {
      newWordId--;
      // console.log(newWordId);
      if (newWordId < startIdx) newWordId = endIdx;

      if (newWordId === wordId) {
        completed = true;
        break;
      }
    }

    setHideMeaning();

    wordId = newWordId;
    status[currentWordSet].lastIdx = wordId;
  };
  const nextWord = () => {
    let newWordId = wordId + 1;
    if (newWordId > endIdx) newWordId = startIdx;
    while (status[currentWordSet].list[newWordId] === true) {
      newWordId++;
      if (newWordId > endIdx) newWordId = startIdx;
      if (newWordId === wordId) {
        completed = true;
        break;
      }
    }
    setHideMeaning();

    wordId = newWordId;
    status[currentWordSet].lastIdx = wordId;
  };
  const updateStatus = () => {
    status[currentWordSet].list[wordId] = true;
    nextWord();
  };
  const toggleMeaning = () => {
    showMeaning = !showMeaning;
  };
  const onKeyPress = (e) => {
    if (["Enter", "ArrowRight", "ArrowDown"].includes(e.code)) nextWord();
    if (["Backspace", "ArrowLeft", "ArrowUp"].includes(e.code)) prevWord();

    if (e.code === "Space") {
      toggleMeaning();
      e.preventDefault();
    }
  };
</script>

<svelte:window on:keydown={onKeyPress} />

<ProgressBar startIdx={startIdx + 1} {progress} endIdx={endIdx + 1} />
<div class="w-64 flex items-center justify-between font-mono text-sm">
  <button
    on:click={prevWord}
    class="w-5/12 bg-white px-4 py-1 rounded-md shadow-md hover:bg-black hover:text-white active:bg-black active:text-white  touch-none"
  >
    previous
  </button>

  <button
    on:click={nextWord}
    class="w-5/12 bg-white px-4 py-1 rounded-md shadow-md
        hover:bg-black hover:text-white active:bg-black active:text-white  touch-none"
  >
    next
  </button>
</div>
<div class="w-64 flex items-center justify-between font-mono text-sm">
  <button
    on:click={updateStatus}
    class="w-full bg-white px-4 py-1 rounded-md shadow-md hover:bg-black hover:text-white active:bg-black active:text-white  touch-none"
  >
    I Know It!
  </button>
</div>
