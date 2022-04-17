<script>
  import { slide } from "svelte/transition";
</script>

<div
  transition:slide
  class=" fixed z-30 h-screen w-screen bg-white text-sm top-0 text-black flex justify-center items-center px-8"
>
  <div class="list-disc w-full max-w-md">
    <h1 class="w-full text-center mb-6 text-xl mx-auto font-mono border-b pb-1">
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
