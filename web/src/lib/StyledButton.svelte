<script>
  export let onClick;
  export let isSelected = false;
  export let text = "";
</script>

<button
  on:click={onClick}
  class={`${
    isSelected ? "bg-black text-white" : "bg-white"
  } px-4 py-1 shadow-md rounded-md font-mono touch-none text-sm`}
>
  {text}
</button>
