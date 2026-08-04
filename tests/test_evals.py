from evals.eval_runner import run_evals


def test_eval_runner_passes_sample_datasets():
    results = run_evals()

    assert results
    assert all(result["passed"] for result in results)

