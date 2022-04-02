<script>
  import "./lib/Tailwind.css";

  import Vocab from "./lib/Vocab.svelte";
  import Credit from "./lib/Credit.svelte";
  import Kanji from "./lib/kanji.svelte";

  let mode = "vocab";

  const setMode = (x) => {
    if (x != mode) mode = x;
  };
</script>

<section class="relative bg-gray-100 w-screen max-w-full min-h-screen">
  <div class="fixed z-20 w-full top-4 flex justify-center gap-2">
    <button
      on:click={() => {
        setMode("vocab");
      }}
      class="font-mono text-sm bg-white px-4 py-1 rounded-md shadow-md
    hover:bg-black hover:text-white active:bg-black active:text-white  touch-none"
    >
      Vocab
    </button>
    <button
      on:click={() => {
        setMode("kanji");
      }}
      class="font-mono text-sm bg-white px-4 py-1 rounded-md shadow-md
    hover:bg-black hover:text-white active:bg-black active:text-white  touch-none"
    >
      Kanji
    </button>
  </div>
  {#if mode == "vocab"}
    <Vocab />
  {:else if mode == "kanji"}
    <Kanji />
  {/if}

  <Credit />
</section>
