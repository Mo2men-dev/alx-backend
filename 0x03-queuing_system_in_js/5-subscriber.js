import { createClient } from 'redis';

const client = createClient();

client.on('error', err => console.log('Redis client not connected to the server: ', err));
client.on('connect', () => console.log('Redis client connected to the server'));

client.on('message', (channel, msg) => {
	console.log(msg);
	if (msg === 'KILL_SERVER') {
		client.unsubscribe(channel);
		client.quit();
	}
});

client.subscribe('holberton school channel');
