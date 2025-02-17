import { print, createClient } from 'redis';

const redisClient = createClient();

redisClient.on('error', (error) => {
  console.log(`Redis client not connected to server: ${error.message}`);
  redisClient.quit();
});
redisClient.on('connect', () => console.log('Redis client connected to the server'));

console.log(redisClient.connected);
/**
 * setting key-value pair in redis
 * @param {string} schoolName -> key
 * @param {string} value      -> value
 */
function setNewSchool(schoolName, value) {
  redisClient.set(schoolName, value, print);
}

/**
 * getting and displaying  value which is associated with the given key
 * at the redis store
 * @param {string} schoolName -> the key for searching in redis
 */
function displaySchoolValue(schoolName) {
  redisClient.get(schoolName, (_error, value) => {
    if (value) console.log(value);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
