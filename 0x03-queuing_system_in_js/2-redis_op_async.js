import { print, createClient } from 'redis';
import { promisify } from 'util';

const redisClient = createClient();

redisClient.on('error', (error) => {
  console.log(`Redis client not connected to server: ${error.message}`);
  redisClient.quit();
});

const getAsync = promisify(redisClient.get).bind(redisClient);

/**
 * setting key-value pair in the redis
 * @param {string} schoolName -> key
 * @param {string} value      -> value
 */
function setNewSchool(schoolName, value) {
  redisClient.set(schoolName, value, print);
}

/**
 * getting and displaying value associated with the given key
 * at the redis store -> asynchronously
 * @param {string} schoolName -> the key to search in redis
 */
async function displaySchoolValue(schoolName) {
  const value = await getAsync(schoolName);
  if (value) console.log(value);
}

/**
 * the entry point
 */
async function main() {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}

redisClient.on('connect', () => {
  console.log('Redis client connected to the server');
  main();
});
