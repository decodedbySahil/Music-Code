const lyrics = [
  ["Main ab kyun hosh mein aata nahi?", 70, 400],
  ["Sukoon yeh dil kyun paata nahi?\n", 50, 600],
  ["Kyun todun khud se jo the waade?", 40, 500],
  ["Ke ab yeh ishq nibhana nahi...\n", 50, 500],
  ["Main modun tumse jo yeh chehra..", 50, 500],
  ["Dobara nazar milana nahi...\n", 50, 500],
  ["Yeh duniya jaane mera dard..", 60, 300],
  ["Tujhe yeh nazar kyun aata nahi?\n", 40, 500]
];

async function printLyrics() {
  console.log("\nPal Pal:\n");

  for (let [line, speed, pause] of lyrics) {
    for (let char of line) {
      process.stdout.write(char);
      await new Promise(r => setTimeout(r, speed));
    }
    console.log();
    await new Promise(r => setTimeout(r, pause));
  }
}

printLyrics();