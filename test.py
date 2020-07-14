import numpy as np

from group_stratifier import GroupStratifiedKFold

n_samples = 1000000
n_classes = 10
n_splits = 4
n_groups = 10000

rng = np.random.RandomState(7)
stratifier = GroupStratifiedKFold(n_splits=n_splits, random_state=12, population_size=200, generations=10)
labels = rng.randint(0, n_classes, n_samples, dtype=np.int32)
groups = rng.randint(0, n_groups, n_samples, dtype=np.int32)
fitness, folds = stratifier.split(labels, groups)
print(fitness)
print(folds)
