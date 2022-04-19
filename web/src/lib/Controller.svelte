<script>
  import ProgressBar from "./ProgressBar.svelte";
  export let startIdx, endIdx, progress;
  export let status, completed, currentWordSet, wordId;
  export let showMeaning;

  export let settings;

  let isRandom = false;
  const toggleRandom = () => {
    isRandom = !isRandom;
  };
  const setHideMeaning = () => {
    showMeaning = false;
  };
  const setShowMeaning = () => {
    showMeaning = true;
  };

  const randWord = () => {
    let oldWordId =
      startIdx + Math.floor(Math.random() * (endIdx - startIdx + 1));
    let newWordId = oldWordId + 1;

    if (newWordId > endIdx) newWordId = startIdx;
    while (status[currentWordSet].list[newWordId] === true) {
      newWordId++;
      console.log(newWordId);
      if (newWordId > endIdx) newWordId = startIdx;
      if (newWordId === oldWordId) {
        completed = true;
        break;
      }
    }
    setHideMeaning();

    wordId = newWordId;
    status[currentWordSet].lastIdx = wordId;
  };
  const prevWord = () => {
    if (isRandom) {
      randWord();
      return;
    }
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
    if (isRandom) {
      randWord();
      return;
    }
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

  const handleShowingMeaning = (toDo, mustShowMeaning) => {
    if (mustShowMeaning) {
      setShowMeaning();
      setTimeout(() => {
        setHideMeaning();
        toDo();
      }, 750);
    } else {
      toDo();
    }
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
    on:click={() => {
      handleShowingMeaning(prevWord, settings.showMeaningBeforeChange);
    }}
    class="text-center w-4/12 bg-white px-2 py-1 rounded-md shadow-md  touch-none"
  >
    previous
  </button>
  <button
    on:click={toggleRandom}
    class={`text-center w-2/12 ${
      isRandom ? "bg-green-500" : "bg-white"
    } px-2 py-1 rounded-md shadow-md
     `}
  >
    🎲
  </button>
  <button
    on:click={() => {
      handleShowingMeaning(nextWord, settings.showMeaningBeforeChange);
    }}
    class={`text-center w-4/12 bg-white px-2 py-1 rounded-md shadow-md  touch-none`}
  >
    next
  </button>
</div>
<div class="w-64 flex items-center justify-between font-mono text-sm">
  <button
    on:click={() => {
      handleShowingMeaning(updateStatus, settings.showMeaningBeforeHide);
    }}
    class="w-full bg-white px-4 py-1 rounded-md shadow-md touch-none"
  >
    I Know It!
  </button>
</div>
