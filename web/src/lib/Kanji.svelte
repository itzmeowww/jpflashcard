<script>
  import n5 from "../data/n5_kanji.json";
  import n4 from "../data/n4_kanji.json";
  import n3 from "../data/n3_kanji.json";
  import n2 from "../data/n2_kanji.json";
  import n1 from "../data/n1_kanji.json";
  import ProgressBar from "./ProgressBar.svelte";

  const words = {
    N5: n5,
    N4: n4,
    N3: n3,
    N2: n2,
    N1: n1,
  };
  let status = {
    N5: {
      lastIdx: 0,
      list: [],
      batches: [],
    },
    N4: {
      lastIdx: 0,
      list: [],
      batches: [],
    },
    N3: {
      lastIdx: 0,
      list: [],
      batches: [],
    },
    N2: {
      lastIdx: 0,
      list: [],
      batches: [],
    },
    N1: {
      lastIdx: 0,
      list: [],
      batches: [],
    },
  };
  let batchSize = 40;
  let currentBatch = 0;
  $: startIdx = status[currentWordSet].batches[currentBatch].start;
  $: endIdx = status[currentWordSet].batches[currentBatch].end;

  $: {
    let cou = 0.0;

    for (let i = startIdx; i <= endIdx; i++) {
      if (status[currentWordSet].list[i] === true) cou = cou + 1;
    }

    progress = cou / (endIdx - startIdx + 1);

    if (cou == endIdx - startIdx + 1) {
      completed = true;
    } else completed = false;
  }

  ["N5", "N4", "N3", "N2", "N1"].forEach((x) => {
    while (status[x].list.length < words[x].length) {
      status[x].list.push(false);
    }
    let cou = Math.ceil(words[x].length / batchSize);

    for (let i = 0; i < cou; i++) {
      status[x].batches.push({
        start: batchSize * i,
        end: Math.min(batchSize * (i + 1) - 1, words[x].length - 1),
      });
    }
  });

  let progress = 0;

  let completed = false;
  let currentWordSet = "N5";
  $: wordId = status[currentWordSet].lastIdx;
  let showMeaning = false;
  $: title = currentWordSet + " Kanji";

  $: word = words[currentWordSet][wordId];

  const setCurrentWordSet = (x) => {
    if (x == currentWordSet) return;
    currentWordSet = x;
    setHideMeaning();

    if (currentBatch != 0) currentBatch = 0;
    wordId = words[x].lastIdx;
  };
  const setCurrentBatch = (x) => {
    // console.log(x);
    if (x == currentBatch) return;
    setHideMeaning();
    currentBatch = x;
    wordId = status[currentWordSet].batches[x].start;
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
  const setHideMeaning = () => {
    showMeaning = false;
  };
  const setShowMeaning = () => {
    showMeaning = true;
  };
  const toggleMeaning = () => {
    showMeaning = !showMeaning;
  };

  const updateStatus = () => {
    status[currentWordSet].list[wordId] = true;
    nextWord();
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
<svelte:head>
  <title>{title}</title>
</svelte:head>
<section class="relative  flex justify-center items-center flex-col gap-4">
  <div
    class="relative  w-screen max-w-full h-screen max-h-screen flex justify-center items-center flex-col gap-4"
  >
    <div>
      <h1 class="text-4xl font-mono touch-none">{title}</h1>
    </div>
    <div class="w-64 px-2 flex justify-between items-center touch-none">
      {#each ["N5", "N4", "N3", "N2", "N1"] as x}
        <button
          on:click={() => {
            setCurrentWordSet(x);
          }}
          class={`${
            currentWordSet == x ? "bg-black text-white" : "bg-white"
          } w-10 shadow-md rounded-md font-mono touch-none`}
        >
          {x}
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
          } w-10 shadow-md rounded-md font-mono touch-none text-sm`}
          >{i + 1}</button
        >
      {/each}
    </div>

    <div
      class="relative w-64 h-40 rounded-lg shadow-md bg-white flex  justify-center items-center overflow-hidden cursor-pointer select-none touch-none"
    >
      <div
        class="left-2 top-2 absolute w-7 h-7 border rounded-full flex items-center justify-center"
      >
        <h1 class="text-xs">{word.num}</h1>
      </div>
      {#if completed}
        <div
          on:click={setHideMeaning}
          class={`bg-black text-white absolute  w-64 h-full flex-col justify-center items-center py-4 gap-2 transition-all flex px-4 text-center`}
        >
          <h1 class="text-md font-light font-mono">Completed</h1>
        </div>
      {:else if showMeaning}
        <div
          on:click={setHideMeaning}
          class={`absolute  w-64 h-full overflow-y-auto flex-col justify-center items-center py-4 gap-2 transition-all flex px-4 text-center`}
        >
          <h1 class="text-md font-light">{word.meaning}</h1>
          <div class="flex flex-col justify-center items-center text-xs gap-1">
            <div class="flex gap-2">
              <h1 class="font-bold">on</h1>
              <h1>{word.on[0].string}</h1>
              <h1>{word.on[1].string}</h1>
            </div>
            <div class="flex gap-2 ">
              <h1 class="font-bold">kun</h1>
              <h1>{word.kun[0].string}</h1>
              <h1>{word.kun[1].string}</h1>
            </div>
          </div>
        </div>
      {:else}
        <div
          on:click={setShowMeaning}
          class={`absolute w-64 h-full flex-col justify-center items-center py-4 gap-2 flex`}
        >
          <h1 class="text-2xl">{word.kanji}</h1>
        </div>
      {/if}
    </div>
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
  </div>
</section>
