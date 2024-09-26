import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('error', err => console.log('Redis client not connected to the server: ', err));

const getAsync = promisify(client.get).bind(client);

const setNewSchool = (schoolName, value) => {
	client.set(schoolName, value, print);
};

const displaySchoolValue = async (schoolName) => {
	const val = await getAsync(schoolName);
	if (val) console.log(val);
};

const main = async () => {
	await displaySchoolValue('Holberton');
	setNewSchool('HolbertonSanFrancisco', '100');
	await displaySchoolValue('HolbertonSanFrancisco');
};

client.on('connect', () => {
	console.log('Redis client connected to the server')
	main();
});
