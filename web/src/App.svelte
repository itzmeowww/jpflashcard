<script>
  import "./lib/Tailwind.css";

  import { slide, blur, fade } from "svelte/transition";

  import Vocab from "./lib/Vocab.svelte";
  import Credit from "./lib/Credit.svelte";
  import Kanji from "./lib/Kanji.svelte";
  import StyledButton from "./lib/StyledButton.svelte";

  let mode = "vocab";

  const setMode = (x) => {
    if (x != mode) mode = x;
  };

  let openSetting = false;
  const toggleSetting = () => {
    openSetting = !openSetting;
  };
</script>

<section
  class="relative bg-gray-100 w-screen min-h-screen flex flex-col justify-center items-center"
>
  <button
    on:click={toggleSetting}
    class={`fixed z-40 right-4 top-4 rounded-full h-8 w-8 shadow-md flex flex-col items-center justify-center ${
      openSetting ? "bg-white" : "bg-black"
    }`}
  >
    {#if openSetting}
      <div
        transition:fade
        class="absolute flex flex-col items-center justify-center"
      >
        <div class="w-5 h-0.5  rotate-45 bg-black" />
        <div class="w-5 -mt-0.5 h-0.5  -rotate-45 bg-black" />
      </div>
    {:else}
      <div
        transition:fade
        class="absolute flex flex-col items-center justify-center gap-1"
      >
        <div class="w-3 h-0.5 bg-white" />
        <div class="w-4 h-0.5 bg-white" />
        <div class="w-3 h-0.5 bg-white" />
      </div>
    {/if}
  </button>
  {#if openSetting}
    <div
      transition:slide
      class="fixed z-30 h-screen w-screen bg-black font-mono text-xl top-0 text-white flex justify-center items-center"
    >
      Stay Tune For Settings...
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
  </div>
  {#if mode == "vocab"}
    <Vocab />
  {:else if mode == "kanji"}
    <Kanji />
  {/if}

  <Credit />
</section>
