<script>
  export let settings;
  import n5 from "../data/n5_vocab.json";
  import n4 from "../data/n4_vocab.json";
  import n3 from "../data/n3_vocab.json";
  import n2 from "../data/n2_vocab.json";
  import n1 from "../data/n1_vocab.json";
  import Controller from "./Controller.svelte";
  import WordSelector from "./WordSelector.svelte";
  import FlashCard from "./FlashCard.svelte";
  const groups = ["N5", "N4", "N3", "N2", "N1"];
  const words = {
    N5: n5,
    N4: n4,
    N3: n3,
    N2: n2,
    N1: n1,
  };
  let status = {};
  groups.forEach((group) => {
    status[group] = {
      lastIdx: 0,
      list: [],
      batches: [],
    };
  });

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
  $: title = currentWordSet + " Vocab";
  $: word = words[currentWordSet][wordId];

  const setCurrentBatch = (x) => {
    currentBatch = x;
    wordId = status[currentWordSet].batches[x].start;
  };

  const setHideMeaning = () => {
    showMeaning = false;
  };
  const setShowMeaning = () => {
    showMeaning = true;
  };
</script>

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
    <FlashCard bind:completed num={word.num} bind:showMeaning>
      <div slot="meaning" class="text-center">
        <h1 class="text-md font-light">{word.meaning}</h1>
        <h1 class="text-xs font-light">({word.type})</h1>
      </div>
      <!-- <h1>{vr.string}</h1> -->
      <div slot="word" class="text-center">
        <h1 class="text-2xl">{word.word}</h1>
        {#if !word.isKatakana && word.reading != word.reading_hiragana}
          <h1 class="text-2xl">{word.reading_hiragana}</h1>
        {/if}
      </div>
    </FlashCard>

    <Controller
      {settings}
      bind:showMeaning
      bind:completed
      bind:currentWordSet
      bind:startIdx
      bind:endIdx
      bind:progress
      {setHideMeaning}
      bind:status
      bind:wordId
    />
  </div>
</section>
