client.on('messageCreate', async (message) => {
  if(message.content.startsWith('!8ball')) {
    const responses = ['Yes', 'No', 'Maybe', 'Absolutely', 'Never', 'Ask again later'];
    const answer = responses[Math.floor(Math.random() * responses.length)];
    message.channel.send(`🎱 ${answer}`);
  }
});
