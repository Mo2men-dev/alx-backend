import { createClient, print } from 'redis';

const client = createClient();

client.on('error', err => console.log('Redis client not connected to the server: ', err));
client.on('connect', () => console.log('Redis client connected to the server'));

const setNewSchool = (schoolName, value) => {
	client.set(schoolName, value, print);
};

const displaySchoolValue = (schoolName) => {
	client.get(schoolName, (_err, val) => {
		if (val) console.log(val);
	});
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
