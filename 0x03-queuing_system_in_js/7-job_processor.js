import { createQueue } from 'kue';

const blacklistedNumbers = ['4153518780', '4153518781'];
const queue = createQueue();

/**
 * handling thenotification jobs for queue "push_notification_code_2"
 * @param {string} phoneNumber -> the user phone number
 * @param {string} message -> pushing the notification message
 * @param {import('kue').Job}} job -> queueing the job
 * @param {import('kue').DoneCallback} done -> done the call back
 * @returns {void}
 */
function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);
  if (blacklistedNumbers.some((number) => number === phoneNumber)) {
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    return;
  }
  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
