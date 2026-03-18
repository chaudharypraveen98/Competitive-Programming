import submitForm from "./submitForm";

export default function App() {
  return (
    <form
      // Ignore the onSubmit prop, it's used by GFE to
      // intercept the form submit event to check your solution.
      onSubmit={submitForm}
      method="POST"
      action="https://questions.greatfrontend.com/api/questions/contact-form"
    >
      <div>
        <label for="name">Name</label><br />
        <input type="text" id="name" name="name" />
      </div>
      <br />
      <div>
        <label for="email">Email</label><br />
        <input type="email" id="email" name="email" />
      </div>
      <br />
      <div>
        <label for="message">Message</label><br />
        <textarea id="message" name="message" />
      </div>
      <br />
      <button type="submit">Send</button>
    </form>
  );
}
