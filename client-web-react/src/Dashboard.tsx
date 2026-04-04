import { useState, useEffect } from 'react'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  LineElement,
  PointElement,
  ArcElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js'
import { Bar, Line, Doughnut } from 'react-chartjs-2'

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  LineElement,
  PointElement,
  ArcElement,
  Title,
  Tooltip,
  Legend,
)

interface ScoreBucket {
  bucket: string
  count: number
}

interface PassRate {
  task: string
  avg_score: number
  attempts: number
}

interface TimelineEntry {
  date: string
  submissions: number
}

interface GroupEntry {
  group: string
  avg_score: number
  students: number
}

interface ItemRecord {
  id: number
  type: string
  title: string
}

async function checkedJson<T>(res: Response): Promise<T> {
  if (!res.ok) throw new Error(`HTTP ${res.status}: ${res.statusText}`)
  return res.json() as Promise<T>
}

function Dashboard({ token }: { token: string }) {
  const [labs, setLabs] = useState<string[]>([])
  const [lab, setLab] = useState('')
  const [scores, setScores] = useState<ScoreBucket[]>([])
  const [passRates, setPassRates] = useState<PassRate[]>([])
  const [timeline, setTimeline] = useState<TimelineEntry[]>([])
  const [groups, setGroups] = useState<GroupEntry[]>([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  // Fetch available labs dynamically from /items
  useEffect(() => {
    const headers = { Authorization: `Bearer ${token}` }
    fetch('/items/', { headers })
      .then((r) => checkedJson<ItemRecord[]>(r))
      .then((items) => {
        const labIds = items
          .filter((i) => i.type === 'lab')
          .map((i) => {
            const m = i.title.match(/Lab\s+(\d+)/i)
            return m ? `lab-${m[1].padStart(2, '0')}` : null
          })
          .filter((id): id is string => id !== null)
          .sort()
        setLabs(labIds)
        if (labIds.length > 0 && !lab) setLab(labIds[labIds.length - 1])
      })
      .catch((err: Error) => setError(err.message))
  }, [token])

  useEffect(() => {
    if (!lab) return
    const headers = { Authorization: `Bearer ${token}` }
    setLoading(true)

    Promise.all([
      fetch(`/analytics/scores?lab=${lab}`, { headers }).then((r) => checkedJson<ScoreBucket[]>(r)),
      fetch(`/analytics/pass-rates?lab=${lab}`, { headers }).then((r) => checkedJson<PassRate[]>(r)),
      fetch(`/analytics/timeline?lab=${lab}`, { headers }).then((r) => checkedJson<TimelineEntry[]>(r)),
      fetch(`/analytics/groups?lab=${lab}`, { headers }).then((r) => checkedJson<GroupEntry[]>(r)),
    ])
      .then(([s, p, t, g]) => {
        setScores(s)
        setPassRates(p)
        setTimeline(t)
        setGroups(g)
        setError('')
      })
      .catch((err: Error) => setError(err.message))
      .finally(() => setLoading(false))
  }, [token, lab])

  if (error) return <p>Error loading analytics: {error}</p>
  if (loading) return <p>Loading analytics...</p>

  const scoreData = {
    labels: scores.map((s) => s.bucket),
    datasets: [
      {
        label: 'Students',
        data: scores.map((s) => s.count),
        backgroundColor: ['#ef4444', '#f59e0b', '#3b82f6', '#22c55e'],
      },
    ],
  }

  const timelineData = {
    labels: timeline.map((t) => t.date),
    datasets: [
      {
        label: 'Submissions',
        data: timeline.map((t) => t.submissions),
        borderColor: '#3b82f6',
        tension: 0.3,
      },
    ],
  }

  const groupData = {
    labels: groups.map((g) => g.group),
    datasets: [
      {
        label: 'Avg Score',
        data: groups.map((g) => g.avg_score),
        backgroundColor: '#3b82f6',
      },
    ],
  }

  const passRateData = {
    labels: passRates.map((p) => p.task),
    datasets: [
      {
        data: passRates.map((p) => p.avg_score),
        backgroundColor: ['#22c55e', '#3b82f6', '#f59e0b', '#ef4444', '#8b5cf6'],
      },
    ],
  }

  return (
    <div>
      <div className="lab-selector">
        <label>Lab: </label>
        <select value={lab} onChange={(e) => setLab(e.target.value)}>
          {labs.map((l) => (
            <option key={l} value={l}>
              {l}
            </option>
          ))}
        </select>
      </div>

      <div className="charts-grid">
        <div className="chart-card">
          <h3>Submissions Timeline</h3>
          <Line data={timelineData} />
        </div>

        <div className="chart-card">
          <h3>Score Distribution</h3>
          <Bar data={scoreData} options={{ plugins: { legend: { display: false } } }} />
        </div>

        <div className="chart-card">
          <h3>Group Performance</h3>
          <Bar data={groupData} options={{ plugins: { legend: { display: false } } }} />
        </div>

        <div className="chart-card">
          <h3>Task Pass Rates</h3>
          <Doughnut data={passRateData} />
        </div>
      </div>

      {passRates.length > 0 && (
        <table>
          <thead>
            <tr>
              <th>Task</th>
              <th>Avg Score</th>
              <th>Attempts</th>
            </tr>
          </thead>
          <tbody>
            {passRates.map((p) => (
              <tr key={p.task}>
                <td>{p.task}</td>
                <td>{p.avg_score}</td>
                <td>{p.attempts}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  )
}

export default Dashboard
