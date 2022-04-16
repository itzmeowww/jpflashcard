<script>
  import "./lib/Tailwind.css";

  import { slide, blur, fade } from "svelte/transition";

  import Vocab from "./lib/Vocab.svelte";
  import Credit from "./lib/Credit.svelte";
  import Kanji from "./lib/Kanji.svelte";
  import Physics from "./lib/Physics.svelte";
  import StyledButton from "./lib/StyledButton.svelte";

  let mode = "vocab";

  let isDarkMode = false;

  const setMode = (x) => {
    console.log(x);
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

  let batchSize = 40;
  let hideCredit = false;
  const setBatchSize = (x) => {
    batchSize = x;
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
    <div
      transition:slide
      class=" fixed z-30 h-screen w-full bg-white text-sm top-0 text-black flex justify-center items-center px-4"
    >
      <div class="w-full max-w-md">
        <h1
          class="w-full text-center border-b pb-1 mb-6 text-xl mx-auto font-mono"
        >
          Settings
        </h1>
        <div class="w-full flex flex-col gap-2 justify-center items-center">
          <div class="flex">
            <h1>Word Size :</h1>
            {#each [40] as x}
              {#if x == batchSize}
                <button class="bg-black text-white px-1 border rounded"
                  >{x}</button
                >
              {:else}
                <button
                  on:click={() => setBatchSize(x)}
                  class="px-1 border rounded">{x}</button
                >
              {/if}
            {/each}
          </div>
          <div class="flex">
            <label for="" class="mr-2">Hide Credit</label>
            <input type="checkbox" bind:checked={hideCredit} name="" id="" />
          </div>
        </div>
      </div>
    </div>
  {/if}

  <button
    on:click={showHelp}
    class={`touch-none fixed z-20 right-4 top-16 rounded-full h-8 w-8 shadow-md flex flex-col items-center justify-center bg-black`}
  >
    <div class="text-white">?</div>
  </button>

  {#if showingHelp}
    <div
      transition:slide
      class=" fixed z-30 h-screen w-screen bg-white text-sm top-0 text-black flex justify-center items-center px-8"
    >
      <div class="list-disc w-full max-w-md">
        <h1
          class="w-full text-center mb-6 text-xl mx-auto font-mono border-b pb-1"
        >
          How to use
        </h1>
        <div class="w-full flex flex-col justify-center items-start gap-2">
          <li class="">
            Tap the card /
            <code class="px-1 bg-black text-white rounded mx-1">Space</code> to switch
            between meaning and vocab
          </li>
          <li class="">
            Tap previous / <code class="mx-1 px-1 bg-black text-white rounded"
              >Left Arrow</code
            > to show the previous vocab
          </li>
          <li class="">
            Tap next / <code class="mx-1 px-1 bg-black text-white rounded"
              >Right Arrow</code
            > to show the next vocab
          </li>
          <li class="">Tap 'I Know It!' to hide the vocab.</li>
        </div>
      </div>
    </div>
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
    <Vocab />
  {:else if mode == "kanji"}
    <Kanji />
  {:else if mode == "physics"}
    <Physics />
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

  {#if !hideCredit}
    <Credit />
  {/if}
</section>
