<script>
  import "./lib/Tailwind.css";

  import { slide, fade } from "svelte/transition";

  import Vocab from "./lib/Vocab.svelte";
  import Credit from "./lib/Credit.svelte";
  import Kanji from "./lib/Kanji.svelte";
  import Physics from "./lib/Physics.svelte";
  import PhysicsChapter from "./lib/PhysicsChapter.svelte";
  import JpLangChapter from "./lib/JpLangChapter.svelte";
  import JpLangChapterRev from "./lib/JpLangChapterRev.svelte";

  import GrammarList from "./lib/GrammarList.svelte";

  import StyledButton from "./lib/StyledButton.svelte";
  import Settings from "./lib/Settings.svelte";
  import Help from "./lib/Help.svelte";

  let settings = {
    showMeaningBeforeHide: false,
    showMeaningBeforeChange: false,
    hideCredit: false,
    batchSize: 40,
    reversed: false,
  };
  let mode = "vocab";
  let selecting = true;

  const setMode = (x) => {
    selecting = false;
    if (x != mode) mode = x;
  };

  let showingHelp = false;
  const showHelp = () => {
    showingHelp = true;
  };
  let showingSetting = false;
  const showSetting = () => {
    showingSetting = true;
  };
  const closeAll = () => {
    showingHelp = false;
    showingSetting = false;
  };

  const setBatchSize = (x) => {
    settings.batchSize = x;
  };

  const flashCards = [
    {
      credit: "JLPT vocab and kanji from",
      url: "https://jlptsensei.com",
      cards: [
        {
          title: "Vocab",
          id: "vocab",
        },
        {
          title: "Kanji",
          id: "kanji",
        },
      ],
    },
    {
      credit: "",
      url: "",
      cards: [
        {
          title: "Physics All",
          id: "physics",
        },
        {
          title: "Physics by Chapter",
          id: "physicschapter",
        },
      ],
    },
    {
      credit: "Vocab from",
      url: "https://jplang.tufs.ac.jp",
      cards: [
        {
          title: "JPlang by chapter",
          id: "jplangchapter",
        },
        {
          title: "JPlang by chapter rev",
          id: "jplangchapterrev",
        },
      ],
    },
    {
      credit: "Sentence Structure from",
      url: "https://jplang.tufs.ac.jp",
      cards: [
        {
          title: "Sentence Structure",
          id: "grammar",
        },
      ],
    },
  ];
</script>

<section
  class="relative bg-gray-100 w-screen min-h-screen flex flex-col justify-center items-center"
>
  <button
    on:click={showSetting}
    class={`touch-none fixed z-20 right-4 top-4 rounded-full h-8 w-8 shadow-md flex flex-col items-center justify-center ${
      showingSetting ? "bg-white" : "bg-black"
    }`}
  >
    <div
      transition:fade
      class="absolute flex flex-col items-center justify-center gap-1"
    >
      <div class="w-3 h-0.5 bg-white" />
      <div class="w-4 h-0.5 bg-white" />
      <div class="w-3 h-0.5 bg-white" />
    </div>
  </button>

  {#if showingHelp || showingSetting}
    <button
      on:click={closeAll}
      class={`touch-none fixed z-40 right-4 top-4 rounded-full h-8 w-8 shadow-md flex flex-col items-center justify-center bg-white`}
    >
      <div
        transition:fade
        class="absolute flex flex-col items-center justify-center"
      >
        <div class="w-5 h-0.5  rotate-45 bg-black" />
        <div class="w-5 -mt-0.5 h-0.5  -rotate-45 bg-black" />
      </div>
    </button>
  {/if}

  {#if showingSetting}
    <Settings bind:settings />
  {/if}

  <button
    on:click={showHelp}
    class={`touch-none fixed z-20 right-4 top-16 rounded-full h-8 w-8 shadow-md flex flex-col items-center justify-center bg-black`}
  >
    <div class="text-white">?</div>
  </button>

  {#if showingHelp}
    <Help />
  {/if}

  {#if selecting}
    <div
      class="flex-1 flex flex-col h-full justify-center items-center w-full gap-4"
    >
      <h1 class="text-lg font-mono">Select Your Flashcard</h1>

      {#each flashCards as flashCard}
        <div class="flex justify-center gap-2 border flex-col rounded p-3 mx-3">
          <div class="flex justify-center gap-2">
            {#each flashCard.cards as card}
              <StyledButton
                onClick={() => {
                  setMode(card.id);
                }}
                text={card.title}
              />
            {/each}
          </div>
          <h1 class="text-center font-mono text-xs">
            {flashCard.credit}
            <a class="text-blue-400" href={flashCard.url}>{flashCard.url}</a>
          </h1>
        </div>
      {/each}
    </div>
  {:else if mode == "vocab"}
    <Vocab {settings} bind:selecting />
  {:else if mode == "kanji"}
    <Kanji {settings} bind:selecting />
  {:else if mode == "physics"}
    <Physics {settings} bind:selecting />
  {:else if mode == "physicschapter"}
    <PhysicsChapter {settings} bind:selecting />
  {:else if mode == "jplangchapter"}
    <JpLangChapter {settings} bind:selecting />
  {:else if mode == "jplangchapterrev"}
    <JpLangChapterRev {settings} bind:selecting />
  {:else if mode == "grammar"}
    <GrammarList bind:selecting />
  {/if}
  <h1 class="mb-3 text-red-500 text-xs font-thin max-w-sm text-center">
    The word list was generated automatically, if you found any error, please
    <a
      href="mailto:winthanasan@gmail.com?subject=Error in JLPT Flashcard website"
      class="underline"
    >
      email</a
    > me.
  </h1>

  {#if !settings.hideCredit}
    <Credit />
  {/if}
</section>
