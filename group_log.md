# **Team open source : Ergo-Guard**   

#                       **Group Log**

| Date / Week | Task / Iteration | Key Findings & Decisions | Outcome & Time Spent |
| :---- | :---- | :---- | :---- |
| **Start Date** | Project selection and initial feasibility check. | **Decision:** Chose "AI-based posture correction" as it integrates AI/ML and addresses a real-world design challenge. **Technical Stack:** Selected Python, MediaPipe, OpenCV, and Streamlit. | Feasibility confirmed. Initial time spent resolving Python environment conflicts (multiple failed installations). |
| **Week 1** | Base Model Integration and initial angle setup. | **Decision:** Used pre-trained **MediaPipe Pose** (Model Complexity 1\) for real-time efficiency. Implemented helper functions (calculate\_angle, angle\_from\_vertical) using NumPy for geometry. | **Working:** Base skeleton tracking functional. Required angle calculation functions completed. |
| **Week 1** | Defining the core ergonomic problem for designers. | **Research:** Identified three distinct faults: *slouching*, *forward head tilt*, and *excessive leaning toward the monitor*. Generic alerts lack diagnostic value. | **Decision:** Must implement a custom, normalized metric to address **forward proximity** specifically. |

## **III. Data Reliability and Final UI Integration (Phase 3\)**

| Date / Week | Task / Iteration | Key Findings & Decisions | Outcome & Time Spent |
| :---- | :---- | :---- | :---- |
| **Week 3** | Implementing **Data Reliability** features. | **Issue:** Metric values flickered due to camera/sensor noise. **Solution:** Implemented **Metric Smoothing (Moving Average)** using a collections.deque buffer (window size adjustable via sidebar). | **Code:** Added smooth\_metrics function to filter raw data, increasing output stability. |
| **Week 3** | Implementing **State Confirmation**. | **Issue:** Rapid status changes (BAD $\\rightarrow$ GOOD $\\rightarrow$ BAD) were visually distracting. **Solution:** Implemented state\_counters. Status must be maintained for **4 consecutive frames** (adjustable in sidebar) before the global state is updated. | **Code:** Updated session state logic to use state\_counters for stability. |
| **Week 3** | Final Streamlit UI and submission checks. | **Design:** Finalized the **sidebar** to include interactive sliders for all thresholds, allowing user personalization and advanced research testing. Added **Session Statistics** tracking to provide users with quantifiable data (percent time in GOOD/WARN/BAD states). | Final app.py created and tested successfully in the local Anaconda environment. |

Here is the structured draft for your **DES646 Group Log**, meticulously detailed to reflect the technical process, challenges, and inventive decisions made during the development of the **Ergo-Guard** application. This log provides the necessary evidence for the 15% weightage.

---

# **🗓️ DES646 Practical Project: Ergo-Guard Group Log**

## **Project: Ergo-Guard: AI-Powered Posture Correction System for Designers**

| Team Members | Suraj Patel(241066) , Nipun Nandwani(240700) , Manas Tripathi(240616) |
| :---- | :---- |
| **Submission Weight** | 15% |

---

## **I. Initial Research and Technical Setup (Phase 1\)**

| Date / Week | Task / Iteration | Key Findings & Decisions | Outcome & Time Spent |
| :---- | :---- | :---- | :---- |
| **Start Date** | Project selection and initial feasibility check. | **Decision:** Chose "AI-based posture correction" as it integrates AI/ML and addresses a real-world design challenge. **Technical Stack:** Selected Python, MediaPipe, OpenCV, and Streamlit. | Feasibility confirmed. Initial time spent resolving Python environment conflicts (multiple failed installations). |
| **Week 1** | Base Model Integration and initial angle setup. | **Decision:** Used pre-trained **MediaPipe Pose** (Model Complexity 1\) for real-time efficiency. Implemented helper functions (calculate\_angle, angle\_from\_vertical) using NumPy for geometry. | **Working:** Base skeleton tracking functional. Required angle calculation functions completed. |
| **Week 1** | Defining the core ergonomic problem for designers. | **Research:** Identified three distinct faults: *slouching*, *forward head tilt*, and *excessive leaning toward the monitor*. Generic alerts lack diagnostic value. | **Decision:** Must implement a custom, normalized metric to address **forward proximity** specifically. |

---

## **II. Inventive Logic and Software Implementation (Phase 2\)**

| Date / Week | Task / Iteration | Key Findings & Decisions | Code Snippet / Design Outcome |
| :---- | :---- | :---- | :---- |
| **Week 2** | Implementing the **Normalized Proximity Ratio (NPR)**. | **Problem:** Pixel distance changes with camera position, making thresholds unreliable. **Solution:** Normalize the distance from the **Nose to the Shoulder Midpoint** against the user's **Shoulder Width** (distance between Left/Right shoulders). | **Code:** Implemented NPR calculation in calculate\_posture\_metrics using np.linalg.norm for normalization. **Outcome:** Metric is now scale-invariant. |
| **Week 2** | Designing the **Three-Tier Classification**. | **Logic:** Defined **three states** (GOOD, WARN, BAD) to provide granular feedback. Set fixed, absolute thresholds for each state based on initial testing (e.g., Neck Angle $\> 45^\\circ$ is BAD). | **Code:** Implemented sequential if/elif logic in the evaluate\_posture function to check all three metrics concurrently. |
| **Week 2** | Designing the **Contextual Feedback Engine**. | **Decision:** Feedback must be **actionable** and use designer terminology. Mapped specific metric failure (e.g., PROXIMITY\_BAD) to prescriptive advice. | **Design:** Drafted FEEDBACK\_MESSAGES dictionary. *Example: Changed generic "Sit up straight" to "Adjust your monitor height" (more actionable and contextual).* |

---

## **III. Data Reliability and Final UI Integration (Phase 3\)**

| Date / Week | Task / Iteration | Key Findings & Decisions | Outcome & Time Spent |
| :---- | :---- | :---- | :---- |
| **Week 3** | Implementing **Data Reliability** features. | **Issue:** Metric values flickered due to camera/sensor noise. **Solution:** Implemented **Metric Smoothing (Moving Average)** using a collections.deque buffer (window size adjustable via sidebar). | **Code:** Added smooth\_metrics function to filter raw data, increasing output stability. |
| **Week 3** | Implementing **State Confirmation**. | **Issue:** Rapid status changes (BAD $\\rightarrow$ GOOD $\\rightarrow$ BAD) were visually distracting. **Solution:** Implemented state\_counters. Status must be maintained for **4 consecutive frames** (adjustable in sidebar) before the global state is updated. | **Code:** Updated session state logic to use state\_counters for stability. |
| **Week 3** | Final Streamlit UI and submission checks. | **Design:** Finalized the **sidebar** to include interactive sliders for all thresholds, allowing user personalization and advanced research testing. Added **Session Statistics** tracking to provide users with quantifiable data (percent time in GOOD/WARN/BAD states). | Final app.py created and tested successfully in the local Anaconda environment. |

---

## **IV. Final Project Parameters (Log Summary)**

### **Final Thresholds Used in app.py**

| Metric | Threshold Type | Value | Interpretation (e.g., Bad/Warning) |
| :---- | :---- | :---- | :---- |
| **Neck Angle** | Bad (Above) | $45.0^\\circ$ | Severe forward head tilt. |
| **Torso Angle** | Bad (Above) | $35.0^\\circ$ | Significant slouching/slumping. |
| **Proximity Ratio (NPR)** | Bad (Below) | $55.0\\%$ | Leaning too close to the screen (NPR is scale-invariant). |
| **Data Smoothing** | Window Size | 8 frames | Moving Average filter length. |
| **Confirmation** | Frames Needed | 4 frames | Frames required to confirm a status change. |

## V. **Project Timeline & Contribution Log (7 Weeks)**

| Week | Task Focus | Key Technical Decisions / Outcome | Responsible Member(s) |
| :---- | :---- | :---- | :---- |
| **1** | **Setup & Base AI** | Confirmed Python/MediaPipe stack. Implemented base angle calculation functions using NumPy. | Manas Tripathi |
| **2** | **Inventive Logic** | Designed and implemented the **Normalized Proximity Ratio (NPR)**. Implemented the initial **Three-Tier Classification** logic. | Nipun Nandwani and Suraj Patel |
| **3** | **Reliability & Design** | Implemented **Metric Smoothing (Moving Average)** using deque to filter noise. Drafted the **Contextual Feedback Engine** messages. | Nipun Nandwani and Suraj patel |
| **4** | **Stability & Logic Finalization** | Implemented **Status Confirmation Logic** (4 consecutive frames) to prevent status flickering. Finalized the concurrent checking of all three metrics. | Nipun Nandwani and Manas tripathi |
| **5** | **UI Refinement** | Finalized **Streamlit UI** (sidebar, \[2.5, 1\] layout). Integrated **sliders** for user-adjustable thresholds. | Suraj Patel |
| **6** | **Evaluation & Test** | Implemented **Session Statistics Module** for measurable data tracking. Conducted internal testing to finalize threshold values (e.g., $55.0\\%$ for NPR). | Nipun Nandwani  |
| **7** | **Final Deliverables** | Recorded the **3-minute presentation video**. Completed **Final Report** and drafted **IPDF/Technical Paper** summary. | Nipun Nandwani, Manas Tripathi and Suraj Patel |

