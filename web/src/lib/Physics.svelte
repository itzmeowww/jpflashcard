<script>
  import physics from "../data/physics.json";
  import Controller from "./Controller.svelte";
  import FlashCard from "./FlashCard.svelte";
  import WordSelector from "./WordSelector.svelte";
  const groups = ["Physics"];
  const words = {
    Physics: physics,
  };
  let status = {
    Physics: {
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

  groups.forEach((x) => {
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
  let currentWordSet = groups[0];
  $: wordId = status[currentWordSet].lastIdx;
  let showMeaning = false;
  $: title = currentWordSet + "";

  $: word = words[currentWordSet][wordId];

  const setCurrentBatch = (x) => {
    // console.log(x);
    if (x == currentBatch) return;
    setHideMeaning();
    currentBatch = x;
    wordId = status[currentWordSet].batches[x].start;
  };

  const setHideMeaning = () => {
    showMeaning = false;
  };
</script>

<svelte:head>
  <title>{title}</title>
</svelte:head>
<section class="relative flex justify-center items-center flex-col gap-4">
  <div
    class="relative  w-screen max-w-full h-screen max-h-screen flex justify-center items-center flex-col gap-4"
  >
    <div>
      <h1 class="text-4xl font-mono touch-none">{title}</h1>
    </div>
    <WordSelector
      parentSetCurrentBatch={setCurrentBatch}
      bind:status
      bind:currentBatch
      bind:currentWordSet
      {groups}
      bind:wordId
      bind:showMeaning
      {words}
    />

    <FlashCard bind:completed num={wordId + 1} bind:showMeaning>
      <div slot="word">
        <h1 class="text-2xl">{word.kanji}</h1>
        <h1 class="text-sm">{word.hiragana}</h1>
      </div>

      <div slot="meaning">
        <h1 class="text-md font-light">{word.meaning}</h1>
      </div>
    </FlashCard>

    <Controller
      bind:showMeaning
      bind:completed
      bind:currentWordSet
      bind:startIdx
      bind:endIdx
      bind:progress
      bind:status
      bind:wordId
    />
  </div>
</section>
