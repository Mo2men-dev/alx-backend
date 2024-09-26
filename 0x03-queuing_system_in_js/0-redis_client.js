import { createClient } from 'redis';

const client = await createClient();

client.on('error', err => console.log('Redis client not connected to the server: ', err));
client.on('conncet', () => console.log('Redis client connected to the server'));
