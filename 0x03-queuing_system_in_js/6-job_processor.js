import { createQueue } from 'kue';

const queue = createQueue();

/**
 * sending notification to the specified user
 * @param {string} phoneNumber  -> the recipient's phone number
 * @param {string} message      -> the message
 */
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});
