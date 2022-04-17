<script>
  import "./lib/Tailwind.css";

  import { slide, fade } from "svelte/transition";

  import Vocab from "./lib/Vocab.svelte";
  import Credit from "./lib/Credit.svelte";
  import Kanji from "./lib/Kanji.svelte";
  import Physics from "./lib/Physics.svelte";
  import StyledButton from "./lib/StyledButton.svelte";
  import Settings from "./lib/Settings.svelte";
  import Help from "./lib/Help.svelte";
  let settings = {
    showMeaningBeforeHide: false,
    showMeaningBeforeChange: false,
    hideCredit: false,
    batchSize: 40,
  };
  let mode = "vocab";

  const setMode = (x) => {
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

  <div class="fixed z-20 top-4 flex justify-center gap-2">
    <StyledButton
      onClick={() => {
        setMode("vocab");
      }}
      text="Vocab"
    />
    <StyledButton
      onClick={() => {
        setMode("kanji");
      }}
      text="Kanji"
    />
    <StyledButton
      onClick={() => {
        setMode("physics");
      }}
      text="Physics"
    />
  </div>
  {#if mode == "vocab"}
    <Vocab {settings} />
  {:else if mode == "kanji"}
    <Kanji {settings} />
  {:else if mode == "physics"}
    <Physics {settings} />
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
