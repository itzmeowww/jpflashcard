<script>
  export let settings, selecting;
  import { slide, fade } from "svelte/transition";
  import jp1 from "../data/1_jplang.json";
  import jp2 from "../data/2_jplang.json";
  import jp3 from "../data/3_jplang.json";
  import jp4 from "../data/4_jplang.json";
  import jp5 from "../data/5_jplang.json";
  import jp6 from "../data/6_jplang.json";
  import jp7 from "../data/7_jplang.json";
  import jp8 from "../data/8_jplang.json";
  import jp9 from "../data/9_jplang.json";
  import jp10 from "../data/10_jplang.json";
  import jp11 from "../data/11_jplang.json";
  import jp12 from "../data/12_jplang.json";
  import jp13 from "../data/13_jplang.json";
  import jp14 from "../data/14_jplang.json";
  import jp15 from "../data/15_jplang.json";
  import jp16 from "../data/16_jplang.json";
  import jp17 from "../data/17_jplang.json";
  import jp18 from "../data/18_jplang.json";
  import jp19 from "../data/19_jplang.json";
  import jp20 from "../data/20_jplang.json";
  import jp21 from "../data/21_jplang.json";
  import jp22 from "../data/22_jplang.json";
  import jp23 from "../data/23_jplang.json";
  import jp24 from "../data/24_jplang.json";
  import jp25 from "../data/25_jplang.json";
  import jp26 from "../data/26_jplang.json";
  import jp27 from "../data/27_jplang.json";
  import jp28 from "../data/28_jplang.json";

  import Controller from "./Controller.svelte";
  import FlashCard from "./FlashCard.svelte";
  import WordSelector from "./WordSelector.svelte";
  let groups = [];
  for (let i = 1; i <= 28; i++) groups.push("jp" + i.toString());
  console.log(groups);
  let words = {
    jp1: jp1,
    jp2: jp2,
    jp3: jp3,
    jp4: jp4,
    jp5: jp5,
    jp6: jp6,
    jp7: jp7,
    jp8: jp8,
    jp9: jp9,
    jp10: jp10,
    jp11: jp11,
    jp12: jp12,
    jp13: jp13,
    jp14: jp14,
    jp15: jp15,
    jp16: jp16,
    jp17: jp17,
    jp18: jp18,
    jp19: jp19,
    jp20: jp20,
    jp21: jp21,
    jp22: jp22,
    jp23: jp23,
    jp24: jp24,
    jp25: jp25,
    jp26: jp26,
    jp27: jp27,
    jp28: jp28,
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
<section
  transition:fade
  class="relative flex justify-center items-center flex-col gap-4"
>
  <div
    class="relative  w-screen max-w-full h-screen max-h-screen flex justify-center items-center flex-col gap-4"
  >
    <button
      on:click={() => {
        selecting = true;
      }}
      class="fixed top-4 underline font-mono">go back</button
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

    <FlashCard bind:completed num={wordId + 1} bind:showMeaning {settings}>
      <div slot="word" class="text-center">
        <h1 class="text-lg">{word.kanji}</h1>
        <h1 class="text-lg">{word.word}</h1>
      </div>

      <div slot="meaning" class="text-center w-full">
        <h1 class="text-md font-light">{word.translation}</h1>
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
      bind:status
      bind:wordId
    />
  </div>
</section>
